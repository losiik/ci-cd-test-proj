from flask import Flask, request

from person import Person
from country import Country

app = Flask(__name__)


PERSON_STORAGE = []
COUNTRY_STORAGE = {}


@app.route('/new_person', methods=['POST'])
def new_person():
    data = request.get_json()

    age = data.get('age')
    height = data.get('height')
    sex = data.get('sex')
    weight = data.get('weight')
    name = data.get('name')

    p = Person(
        age=age,
        height=height,
        sex=sex,
        weight=weight,
        name=name
    )

    PERSON_STORAGE.append(p)

    return {'success': True}


@app.route('/new_country', methods=['POST'])
def new_country():
    data = request.get_json()

    age_for_alco = data.get('age_for_alco')
    name = data.get('name')

    c = Country(
        age_for_alco=age_for_alco,
        name=name
    )

    COUNTRY_STORAGE['name'] = c

    return {'success': True}


@app.route('/persons', methods=['GET'])
def get_persons():

    person_arr = []
    for person in PERSON_STORAGE:
        person_arr.append(
            {'name': person.name, 'age': person.age}
        )
    return {'persons': person_arr}


if __name__ == '__main__':
    app.run(debug=True)
