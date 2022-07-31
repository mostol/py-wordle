from db.repository import *
import mysql.connector


class MysqlRepository(Repository):

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # default: 'db'. Local: 'localhost'.
            'port': '32000',  # Default: '3306'. Local: '32000'.
            'database': 'wordle'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def load_lexicon(self) -> list[str]:
        sql = 'SELECT * FROM lexicon'
        self.cursor.execute(sql)

        return [word for (id,word) in self.cursor]
