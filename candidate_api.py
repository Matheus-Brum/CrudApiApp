from candidateDAO import CandidateDAO
from flask_restful import Resource
from flask import jsonify, request, redirect


class CandidateListApi(Resource):
    # Endpoint for a list of candidates
    def get(self):
        return jsonify(CandidateDAO().get_all_candidates())

    def post(self):
        id = request.form['id']
        name = request.form['name']
        phone_no = request.form['phone_no']
        email = request.form['email']
        salary = request.form['salary']
        position = request.form['position']
        comment = request.form['comment']

        if is_numeric(id) is False or is_numeric(phone_no) is False or is_numeric(salary) is False or\
            has_empty([id, name, phone_no, email, salary, position, comment]) is False or\
                len(id) > 10 or len(phone_no) != 10:
            return redirect('/error', code=302)
        else:
            candidate = {'id': id, 'name': name, 'phone_no': phone_no,
                         'email': email, 'salary': salary, 'position': position,
                         'comment': comment}
            if CandidateDAO().candidate_exists(candidate['id']) == False:
                CandidateDAO().add_candidate(candidate)
                return redirect('/success', code=302)
            else:
                return redirect('/error', code=302)


class CandidateApi(Resource):
    # Endpoint for a single candidate
    def get(self, id):
        return jsonify(CandidateDAO().get_candidate(id))

    def post(self, id):
        id = request.form['id']
        name = request.form['name']
        phone_no = request.form['phone_no']
        email = request.form['email']
        salary = request.form['salary']
        position = request.form['position']
        comment = request.form['comment']

        if is_numeric(id) is False or is_numeric(phone_no) is False or is_numeric(salary) is False or\
            has_empty([id, name, phone_no, email, salary, position, comment]) is False or\
                len(id) > 10 or len(phone_no) != 10:
            return redirect('/error', code=302)
        else:
            candidate = {'id': id, 'name': name, 'phone_no': phone_no,
                         'email': email, 'salary': salary, 'position': position,
                         'comment': comment}
            if CandidateDAO().candidate_exists(candidate['id']) == True:
                CandidateDAO().update_candidate(candidate)
                return redirect('/success', code=302)
            else:
                return redirect('/error', code=302)


def has_empty(values):
    for value in values:
        if value == '' or value is None:
            return False
    return True


def is_numeric(value):
    if value.isnumeric() is True:
        return True
    else:
        return False