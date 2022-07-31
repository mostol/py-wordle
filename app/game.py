import string
from enum import Enum


class PositionState(Enum):
    ABSENT = 0
    UNK = 1
    PRESENT = 2


class Game:

    def __init__(self, lexicon, state=None):
        self.lexicon = lexicon
        self.state = state

        # `characters` could probably be abstracted to not just use the English alphabet.
        self.letters = Enum("Letter", [*string.ascii_uppercase])


class GameState:

    def __init__(self, letter_states):
        # A dict which, for each valid letter in the game, maps to
        # that letter's `PositionState`s. So if the letter `A` was
        # guessed in the first spot, and it came back yellow, then
        # `self.letter_states["A"] = [ABSENT, UNK, UNK, UNK, UNK]`.
        # Or if "S" were guessed in the third spot and came back green,
        # we would have `self.letter_states["S"] = [UNK, UNK, PRESENT, UNK, UNK]`.

        self.letter_states = letter_states

    # def from_guesses(self):
        # Create a `GameState` from guesses.
