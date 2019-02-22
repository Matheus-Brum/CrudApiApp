import sqlite3
from candidate import *

# USAGE OF PLACEHOLDERS '?' TO PREVENT SQL INJECTION


class CandidateDAO:

    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('database/db_prod.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_all_candidates(self):
        candidates = []
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT *"
                       "FROM Candidates")
        candidate_tuples = cursor.fetchall()
        for row in candidate_tuples:
            candidate = Candidate(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).serialize()
            candidates.append(candidate)
        return candidates

    def get_candidate(self, id):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT *"
                       "FROM Candidates "
                       "WHERE Id = ?", (id,))
        result = cursor.fetchone()
        candidate = Candidate(result[0], result[1], result[2], result[3], result[4], result[5], result[6]).serialize()
        return candidate

    def add_candidate(self, candidate):
        cursor = self.get_connection().cursor()
        cursor.execute("INSERT INTO Candidates"
                       "(Id, Name, Phone_no, Email, Salary, Position, Comment)"
                       "VALUES(?,?,?,?,?,?,?)",
                       (candidate['id'], candidate['name'], candidate['phone_no'],
                        candidate['email'], candidate['salary'], candidate['position'],
                        candidate['comment']))
        self.connection.commit()

    def update_candidate(self, candidate):
        cursor = self.get_connection().cursor()
        cursor.execute("UPDATE Candidates "
                       "SET Name = ?, Phone_no = ?, Email = ?, Salary = ?, Position = ?, Comment =? "
                       "WHERE Id = ?",
                       (candidate['name'], candidate['phone_no'],
                        candidate['email'], candidate['salary'], candidate['position'],
                        candidate['comment'], candidate['id']))
        self.connection.commit()

    def candidate_exists(self, id):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT Id "
                       "FROM Candidates "
                       "WHERE Id = ?", (id,))
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True
