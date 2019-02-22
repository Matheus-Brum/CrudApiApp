from flask import Flask, g, render_template
from flask_restful import Api
import requests
import candidateDAO
from candidate_api import *

app = Flask(__name__)
app.static_folder = 'static'
api = Api(app)
api.add_resource(CandidateListApi, '/api/candidates')
api.add_resource(CandidateApi, '/api/candidates/<id>')


@app.route('/')
def home():
    candidates = requests.get('http://127.0.0.1:5000/api/candidates').json()
    return render_template('home.html', candidates=candidates)


@app.route('/add_candidate')
def add_candidate():
    return render_template('add_candidate.html')


@app.route('/find_candidate')
def find_candidate():
    return render_template('find_candidate.html')


@app.route('/candidates/<id>')
def update_candidate(id):
    candidate = CandidateDAO().get_candidate(id)
    return render_template('update_candidate.html', candidate=candidate)


@app.route('/api')
def api_entry_point():
    return render_template('api_entry_point.html', title='API')


@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/success')
def success():
    return render_template('success.html')


# function sets global context database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
            g._database = candidateDAO.CandidateDAO()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()
