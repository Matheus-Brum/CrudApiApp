DROP TABLE Candidates;

CREATE TABLE Candidates(
    Id	integer PRIMARY KEY AUTOINCREMENT,
	Name	varchar ( 40 ),
	Phone_no	varchar ( 10 ),
	Email	varchar ( 40 ),
	Salary    integer,
	Position    varchar(25),
	Comment   TEXT
);

INSERT INTO Candidates VALUES(1, 'Matheus Brum', '5148065026', 'matheus.esbrum@gmail.com', 20000, 'Order Picker', 'This guy is a beast!');
INSERT INTO Candidates VALUES(2, 'John Doe', '4380909123', 'john-doe@gmail.com', 40000, 'Vice-President', 'I''m the king when the President is not around.');
INSERT INTO Candidates VALUES(3, 'Jane Doe', '5148004321', 'jane-doe@gmail.com', 80000, 'President', 'Hey! Go to work everyone!');