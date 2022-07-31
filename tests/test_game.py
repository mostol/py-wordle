from app.game import *
from db.mysql_repository import *
import pytest


def test_game():
    database = MysqlRepository()
    lexicon = database.load_lexicon()
    game = Game(lexicon)

    assert isinstance(game, Game)
