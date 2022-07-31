from db.mysql_repository import *

def test_database():
    sql_repo = MysqlRepository()
    assert isinstance(sql_repo, Repository)

    lexicon = sql_repo.load_lexicon()
    assert isinstance(lexicon,list)
    assert lexicon[0] == "cigar"
