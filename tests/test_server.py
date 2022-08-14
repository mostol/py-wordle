import requests

# curl --header "Content-Type: application/json" \
#   --request POST \
#   --data '{"word1":"hello","val1":["b","g","g","g","g"]}' \
#   http://localhost:5000/guess


def test_connection():
    try:
        r = requests.post("http://localhost:5000/guess")
    except ConnectionError:
        raise ValueError("Connection couldn't be made. Is `app.py` running?")


def test_results():
    headers = {'Content-Type': "application/json"}
    r = requests.post("http://localhost:5000/guess",
                      json={"word1": "hello", "val1": ["b", "g", "g", "g", "g"]})
    result = r.json()["result"]

    assert result is not "hello" # Based on the info passed, "hello" should be impossible.
    assert result in {"jello", "jello"}  # Answer should be one of these.
