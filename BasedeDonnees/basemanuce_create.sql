PRAGMA encoding = 'UTF-8';

CREATE TABLE printer (
	id 			INTEGER PRIMARY KEY,
	name		TEXT NOT NULL,
	birthyear	INTEGER,
	deathyear	INTEGER
);

CREATE TABLE institution (
	id 			INTEGER PRIMARY KEY,
	country 	TEXT NOT NULL,
	city		TEXT NOT NULL,
	institution_name	TEXT NOT NULL
);

CREATE TABLE books (
	id 			INTEGER PRIMARY KEY,
	title		TEXT,
	printdate	INTEGER,
	format		TEXT,
	language	TEXT,
	identifier	TEXT NOT NULL,
	printer_id INTEGER NULL REFERENCES printer(id),
	institution_id INTEGER NULL REFERENCES institution(id)
);
