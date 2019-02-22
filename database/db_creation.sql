CREATE TABLE Candidates(
    Id	integer PRIMARY KEY AUTOINCREMENT,
	Name	varchar ( 40 ),
	Phone_no	varchar ( 10 ),
	Email	varchar ( 40 ),
	Salary    integer,
	Position    varchar(25),
	Comment   TEXT
);