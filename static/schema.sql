drop table if exists entries;
create table apply (
	id integer primary key autoincrement,
	name text not null,
	email text not null,
	grade text not null,
	position text not null,
	project text not null,
	skills text not null,
	comments text not null,
	task text not null
);