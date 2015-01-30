DROP TABLE IF EXISTS application;
CREATE TABLE application (
	appId INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	email TEXT NOT NULL,
	grade TEXT NOT NULL,
	position TEXT NOT NULL,
	project TEXT NOT NULL,
	skills TEXT NOT NULL,
	comments TEXT NOT NULL,
	task TEXT NOT NULL,
	timestamp DATE NOT NULL
);
