from app.game import *
import pytest


# Tests go here. This is just a filler :)
def test_wordlist():
    lexicon = get_lexicon("wordlist.txt")

    assert isinstance(lexicon, list)
    assert isinstance(lexicon[0], str)
    assert lexicon[0] == "cigar"
