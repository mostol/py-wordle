import db.mysql_repository
from app.game import *


class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()
        lexicon = self.repo.load_lexicon()

        # By default, an empty game with no guesses is started.
        self.game = Game(lexicon)

    # Use Case 1: User can start a game with a specific game state, based on existing guesses and
    # the associated results.
    # Expects a list of tuples.
    def add_guesses(self, guesses):
        self.game.add_guesses(guesses)

    # Use Case 1, pt 2: User can get a "best guess".
    # Note that this doesn't apply for Use Case 2, because the current metrics
    # think that any guess is just as good as any other.
    def get_best_guess(self):
        return self.game.get_best_guess()


# Service layer as entrypoint?
if __name__ == "__main__":
    services = Services()
