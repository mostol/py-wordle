import db.mysql_repository


class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()
        