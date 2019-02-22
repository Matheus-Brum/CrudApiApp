# CrudApiApp
Please read the entire document, especially the last part 
for a quick demo.
## TODO
- Validations (Front End and Back End)
- Cross Site Request Forgery Protection
- Post-Redirect-Get
- Add some documentation
- Make UI prettier
- If there is still time, make the app at least bilingual
- If there is still time, make selenium demo/tests

## Questions 
- Find equivalent of a search? (check)
- Save equivalent of an update? (check)
- In memory? (check)
- SQL vs ORM? (check)
- unit tests? (check)
- early or late but better? (check)

## Installation/Packages
Virtual environment not added to avoid compatibility issues.
Instead, requirements.txt indicates the project requirements.

## What would I change?
- If the app was bigger and more complex, I would create
Blueprints for the views/controllers so I can have a 
directory of views/controllers containing the .py files 
of each view and importing them to the app.py thus creating 
a more robust app and a better
project structure.
- Make a feature so the app can support multiple languages in a scalable way.
To do so, I would make a languages module containing language dictionaries to 
use with the template engine instead of static text.
- Add unit testing to the app if the app becomes more complex.
- Find a solution for lack of reusability for the front end form
validation methods.
- Forgot to add Cross Site Request Forgery Protection

## Running the app
from the source of the app, run "set FLASK_APP=app.py" and then "flask run".

## For the lazy ones
Run the demo.py script located inside the folder (using the command "python demo.py"),
sit back and enjoy your coffee. The demo uses Google Chrome web browser and executes 
the 3 main features of the app.

