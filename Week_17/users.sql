CREATE TABLE users (
	username varchar(100),
	password varchar(100),
	email varchar(100),
    woonplaats varchar(100)
)

INSERT INTO users (username, email, woonplaats)
VALUES ('Bob', 'bob@martin.nl', 'Den Haag'),
       ('Swen', 'swen@mulderij.nl', 'Utrecht'),
	   ('Jane', 'jane@doe.nl', 'Utrecht')

CREATE TABLE locaties (
	plaatsnaam varchar(100),
	bezorging bit
	)		

INSERT INTO locaties
VALUES ('Utrecht', '1'),
        ('Den Haag', '0')
       