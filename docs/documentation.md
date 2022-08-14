# PyWordle Documentation
PyWordle is a Wordle solution generator. Put initial guesses in, and an "optimal" guess comes out.

## Manual setup
First, run `docker compose up` in the main `py-wordle` directory to get the SQL database up and running.

Then, ensure all dependencies (listed in `requirements.txt`) are installed, and run `app.py`. You should now be
good to go!

## Contextual best guess
You can pass in previous guesses, and PyWordle will return the best guess. Previous guesses are formulated as
word/status pairs, (i.e. a word is paired with a list of statuses that reflect the info Wordle gives you about
 each letter). The word is just a string, and the letter statuses are a list/array of letters that correspond to
on of three states: `g` (green in-game; the letter is in the correct position), `y` (yellow; the letter is in the
word but not in this position), and `b` (black; the letter is not in the word). 

The word and the status list must be the same length. 

Output is a single word.

### Web UI
Using `web/py-wordle.html`, you can input a guess via a snazzy web-based interface. Type in your word, then use
the dropdown menus to select the status/color of each letter in the word. Hit `Submit` to get your result, (which
will appear in the `Result:` area).

#### Example
Word: `hello`<br/>
Letter colors: `Black` `Green` `Green` `Green` `Green`

Result: `jello`

### Direct access
You can use `curl` or similar tools to access the API directly via a `POST` request to `"http://localhost:5000/guess"`. 
The word/status pair must be formatted as JSON, where the word has the key `word1`, and the values are given as an 
array with key `val1` and each color/status is either `"b"`, `"g"`, or `"y"`. The header should 
be `Content-Type: application/json`.

A JSON response is returned, containing the best-guess word.

#### Example
A `curl` request:

```commandline
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"word1":"hello","val1":["b","g","g","g","g"]}' \
  http://localhost:5000/guess
```

Result:
```json
{"result": "jello"}
```

## Empty game best guess
The ability to suggest a "best guess" without any other context whatsoever is not yet implemented.