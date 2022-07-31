CREATE DATABASE wordle;
use wordle;

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT, # I assume having an ID might be useful somewhere.
    word CHAR(5), # All words should have the same length.
    PRIMARY KEY (id)
);

LOAD DATA LOCAL INFILE "/docker-entrypoint-initdb.d/wordlist.txt" 
    INTO TABLE lexicon
    (word);