class Candidate:
    def __init__(self, id, name, phone_no, email, salary, position, comment):
        self.id = id
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.salary = salary
        self.position = position
        self.comment = comment

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_no': self.phone_no,
            'email': self.email,
            'salary': self.salary,
            'position': self.position,
            'comment': self.comment
        }
