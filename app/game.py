from collections import defaultdict


class Game:

    def __init__(self, lexicon, guesses=None):

        # Maybe a set would be best here?
        self.lexicon = set(lexicon)

        # All words need to be the same length
        lengths = {len(word) for word in lexicon}
        if len(lengths) != 1:
            raise ValueError("All words in lexicon must be of the same length; found multiple lengths.")
        self.length = lengths.pop()  # The length of words in the game.

        # We *might* want to check that all of the guesses were valid words from the lexicon. Or maybe not!
        self.state: GameState = GameState(guesses)

        self.solution_space = {word for word in self.lexicon if self.is_possible(word)}

    # Determine if a word is a *possible* solution to the game, given its current state.
    def is_possible(self, word):

        if len(word) != self.length:
            raise ValueError("Word must be the correct length.")

        if word not in self.lexicon:
            raise ValueError("Word must be an existing word in the lexicon.")

        # A word is possible as long as none if its letters are *im*possible. `True` means
        # that letter is in that position, and `None` means we don't know, so as long as
        # all the elements are *not `False`*, the word is possible.
        return all(self.state[position_pair] is not False for position_pair in enumerate(word))

    # Currently, a **very** naive calculation of the "best" guess.
    # Returns the word in the `solution_space` that has the highest "fit score", based on
    # the `GameState`'s `fit_score` function. ...It's a start!
    def get_best_guess(self):
        return max((word for word in self.solution_space), key=self.state.fit_score)

    # Update the current game with a newer game state.
    # Note to self: make sure there aren't any potential issues with conflicting game state details...
    def add_guesses(self, guesses):
        new_state = GameState(guesses).game_state
        self.state.game_state.update(new_state)


class GameState:

    # To initialize a `GameState`, pass in a list of "guesses", which are a tuple
    # of `(string, statuses)` where `string` is the word that was guessed, and `statuses`
    # is a list of one-letter strings that says which color each letter in the string was
    # (either `"g"` (green), `"y"` (yellow), or `"b"` (black/gray).
    def __init__(self, guesses=None):
        # !Update! `game_state` is now a dict of positions (plus "absent"), which map to
        # sets of letters. These letters indicate possibilities (or "known"s).
        # But wait! The "if it's not in the set, it's not possible" angle does throw a small
        # wrench in flexibility, because then we'd need to explicitly list un-guessed letters (meaning
        # we'd need a list of all possible letters beforehand).
        #
        # We'll also have a "present" set, for yellow letters. The rationale here is that
        # we want to quickly check if a word matches the criteria, and the value that yellow
        # letters gives us is that it tells us a letter *must* be in the word somewhere. That filters
        # out a lot of words, potentially, but it's cumbersome to notate that within the individual position
        # entries.
        self.game_state = {defaultdict(set)}

        if guesses is not None:
            # For fun, we'll keep a list of what the guesses were.
            self.guesses = guesses

            # May want an actual mechanism to check correct formation of input...
            for guess in guesses:
                word, letter_states = guess

                if len(word) != len(letter_states):
                    raise ValueError("Number of letters and number of states do not match.")

                for pos, (letter, state) in enumerate(zip(*guess)):
                    pos_set = self.game_state[pos]  # (To avoid repetition)
                    if state.lower() == "g":
                        # We know that this position has this letter in it, for sure,
                        # and
                        pos_set.clear.add(letter)
                        # (However, that says nothing about that letter in other positions of the word, btw.)
                    elif state.lower() == "b":
                        # We know this letter is not in *any* position.
                        # (Aside from positions we already know it's in.)
                        self.game_state["missing"].add(letter)
                    elif state.lower() == "y":
                        # We know this letter is not in *this* position.
                        pos_set.add(letter)
                        # We know it's somewhere else in the word, though.
                        for position, contents in set(self.game_state).difference([pos,"absent"]):
                            contents.add(letter)

                    else:
                        raise ValueError("Unknown letter state encountered. Should be 'g', 'y', or 'b'.")
        else:
            self.guesses = []

    # Returns a "fitness" score for a word, given the game state.
    # This is just an initial, naive attempt at coming up with a "best match" criterion.
    def fit_score(self,word):
        score = 0
        for pos, letter in enumerate(word):
            state = self[(pos, letter)]

            # Add 1 to the score if position matches...
            if state:
                score += 1
            # If the letter isn't flat-out wrong in this spot for sure...
            elif state is None:
                # Add 0.25 if the letter hasn't been guessed yet at all
                if len(self.game_state[letter]) == 0:
                    score += 0.25
                # Add 0.75 if the letter has been guessed at some point (which means it's yellow,
                # or is being masked by a separate green instance and could still be in the word).
                else:
                    score += 0.25
            # ...and add nothing if the state is False (letter is not in this position, for sure).

        return score

    # Current API is to index into a `GameState` via a position/letter tuple.
    # I think I would prefer `(letter, pos)`, but that goes against how `enumerate` naturally works,
    # and it's not a huge deal for it to be flexible at the moment.
    def __getitem__(self, letter_pos):

        pos, letter = letter_pos

        # Default to empty dict if letter hasn't been added to the game state yet.
        # The end result: we get `True` if that letter is in that position,
        # `False` if it is decidedly *not* in that position, and
        # `None` if we don't know yet.
        return self.game_state.get(letter, {}).get(pos)

    # ~~ A note on the `game_state` setup:
    # We could have the dict's first layer be letters, or we could have it be positions. (Assuming we're not
    # putting it all in a matrix or something instead).
    #
    # Right now I have it set up with letters as the first
    # layer. This makes it easy to set a whole letter's state to `False` if we have a  "black" letter that
    # isn't in the word (which is also a common thing to happen, most letters are *not* part of the word).
    # It also makes it easy to tell which letter's haven't been guessed yet (they'll just not be in the dict).
    #
    # It *does* make it a little harder to deal with the case when we *know* a letter/position combo. When that
    # happens, we want to be able to mark that letter/position combo as `True`, but if that's the case, we also
    # definitively know that all other letters in that position are also `False`. So maybe we really do need to
    # index by position. If we did that, we could set a `defaultdict` or something so that all other letters
    # default to `False`.
    #
    # One possibility would be to have "external" info, like a datastructure that says whether a letter is
    # in the word, or whether a position is known or not.
    #
