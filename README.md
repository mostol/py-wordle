# PyWordle
A [Wordle](https://www.nytimes.com/games/wordle/index.html) solution-generator in Python, initially built for LING508 in the University of Arizona HLT program.

## Use cases
[ ] Users can provide a game state (i.e. which letters have already been guessed and what the results were), and the best solution will be returned.
	* *Input*: Game state
	* *Output*: The optimal guess to make (based on known possible solutions)
[ ] If a blank game state is provided, the best "first guess" is returned.
	* *Input*: Nothing (blank game state)
	* *Output*: Optimal first guess

### Future use case ideas
* Selectable, alternative metrics/heuristics for "best". (For example, there may be a difference between "What word is most likely to be the solution?" and "What word will narrow down my options most strategically?")
* Return multiple guesses, instead of just "the best", so people can pick from some options? Maybe also provide a numeric metric alongside results so people can gauge how well each choice is expected to perform.
* From a UI standpoint, there are a few options for representing the game state. You could input all of your guesses so far along with the color-coded results. You could also input the info on a per-letter basis (like the keyboard representation) instead of a per-guess basis. Maybe this could be user-selectable.
* The live, *New York Times* version of Wordle draws from the word list every day, and does not repeat words (as far as I know). One potential feature would be to take a list of previous solutions and use that as a basis for a "best initial guess", with the assumption that words won't be reused any time soon.