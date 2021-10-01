import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    housing_median_age = db.Column(db.Float)
    total_rooms = db.Column(db.Float)
    total_bedrooms = db.Column(db.Float)
    population = db.Column(db.Float)
    households = db.Column(db.Float)
    median_income = db.Column(db.Float)
    median_house_value = db.Column(db.Float)
    ocean_proximity =  db.Column(db.String)

    def __repr__(self) -> str:
        return f"""
        id :{self.id}
        longitude : {self.longitude}
        latitude : {self.latitude}
        housing_median_age : {self.housing_median_age}
        total_rooms : {self.total_rooms} 
        total_bedrooms : {self.total_bedrooms}
        population : {self.population}
        households : {self.households}
        median_income : {self.median_income}
        median_house_value : {self.median_house_value}
        ocean proximity : {self.ocean_proximity} 
        """


@app.route('/')
def home():
    return '<p>api</p>'


@app.route('/api/v1/data/housing', methods=['POST'])
def add_home():
    data = request.json
    home = Home(
        longitude = data['homes']['longitude'],
        latitude = data['homes']['latitude'],
        housing_median_age = data['homes']['housing_median_age'],
        total_rooms = data['homes']['total_rooms'],
        total_bedrooms = data['homes']['total_bedrooms'],
        population = data['homes']['population'],
        households = data['homes']['households'],
        median_income = data['homes']['median_income'],
        median_house_value = data['homes']['median_house_value'],
        ocean_proximity = data['homes']['ocean_proximity']
    )
    try:
        db.session.add(home)
        db.session.commit()
    except:
        raise Exception('Failure to add resource.')
    return {"message": "Successfully added resource"}


@app.route('/api/v1/data/housing/<int:id>', methods=['GET'])
def get_home(id):
    home = Home.query.get_or_404(id)
    return {'id':home.id, 'longitude':home.longitude , 'latitude':home.latitude, 'housing_median_age':home.housing_median_age,
            'total_rooms':home.total_rooms,'total_bedrooms':home.total_bedrooms, 'population':home.population,
            'households':home.households, 'median_income':home.median_income, 'median_house_value':home.median_house_value,
            'ocean_proximity':home.ocean_proximity
    }


@app.route('/api/v1/data/housing/<int:id>', methods= ['DELETE'])
def delete_home(id):
    home = Home.query.get(id)
    if home is None:
        return {"error": "id not found in database"}
    try:
        db.session.delete(home)
        db.session.commit()
    except:
        raise Exception('Failure to delete resource.')

    return {"message": "Successfully deleted resource"}


@app.route('/api/v1/data/housing/<int:id>', methods=['PUT'])
def update_home(id):
    home = Home.query.get_or_404(id)
    data = request.json
    home.longitude = data['homes']['longitude'],
    home.latitude = data['homes']['latitude'],
    home.housing_median_age = data['homes']['housing_median_age'],
    home.total_rooms = data['homes']['total_rooms'],
    home.total_bedrooms = data['homes']['total_bedrooms'],
    home.population = data['homes']['population'],
    home.households = data['homes']['households'],
    home.median_income = data['homes']['median_income'],
    home.median_house_value = data['homes']['median_house_value'],
    home.ocean_proximity = data['homes']['ocean_proximity']
    try:
        db.session.commit()
    except:
        raise Exception('Failure to update resource.')

    return {"message":"Update resource Success"}


if __name__ == '__main__':
    app.run(debug=True)
