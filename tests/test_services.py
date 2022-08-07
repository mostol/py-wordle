from app.services import *
from db.mysql_repository import *
import pytest


def test_services():
    s = Services()

    assert isinstance(s.repo, MysqlRepository)
    assert isinstance(s.get_best_guess(), str)

    s.add_guesses([("helps", ['g', 'g', 'g', 'b', 'b']),
                   ("cello", ['b', 'g', 'g', 'g', 'g'])])

    best_guess = s.get_best_guess()
    assert isinstance(best_guess, str)
    assert best_guess == "hello"
