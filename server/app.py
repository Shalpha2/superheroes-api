from flask import Flask, make_response,request
from flask_migrate import Migrate
from models import db, Hero, HeroPower, Power

app= Flask(__name__ )

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hero_power.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

migrate=Migrate(app,db)
db.init_app(app)


#get heroes
@app.route('/heroes' , methods = ['GET'])
def get_heroes():
    heroes = [hero.to_dict(rules=('-hero_powers',)) for hero in Hero.query.all()] 
     
    return make_response(heroes, 200)
    
    #get heroes by id
@app.route('/heroes/<int:id>' , methods = ['GET'])
def get_hero_by_id(id):
    hero=Hero.query.get(id)
    if  not hero:
        return make_response({"error": "Hero not found"}, 404)
    
    hero_dict = hero.to_dict(rules=('hero_powers', 'hero_powers.power'))

    return make_response(hero_dict,200)


#get powers 
@app.route('/powers' , methods = ['GET'])
def get_powers():
    
    powers = [power.to_dict(rules=('-hero_powers',)) for power in Power.query.all()]
    
    return make_response(powers, 200)
    

#get powers by id

@app.route('/powers/<int:id>' , methods = ['GET'])
def get_power_by_id(id):
    power=Power.query.get(id)
    if  not power:
        return make_response({"error": "Power not found"}, 404)
    return make_response(power.to_dict(rules=('-hero_powers',)),200)


#patch powers by id

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)

    if not power:
        return make_response({"error": "Power not found"}, 404)

    data = request.get_json()

    if "description" in data:
        try:
            power.description = data["description"]
        except ValueError as e:
            return make_response({"errors": [str(e)]}, 400)

    db.session.commit()
    return make_response(power.to_dict(rules=('-hero_powers',)), 200)


      
    #post hero_powers

@app.route('/hero_powers', methods=['POST'])
def add_heropower():
    data = request.get_json()

    try:
        # Extract and validate fields
        strength = data.get('strength')
        power_id = data.get('power_id')
        hero_id = data.get('hero_id')

        if not all([strength, power_id, hero_id]):
            raise ValueError("All fields: strength, power_id, and hero_id are required.")

        # Create new HeroPower (strength validation handled by model)
        new_hero_power = HeroPower(
            strength=strength,
            power_id=power_id,
            hero_id=hero_id
        )
        db.session.add(new_hero_power)
        db.session.commit()

        # Prepare detailed response with hero and power data
        response_data = {
            "id": new_hero_power.id,
            "hero_id": new_hero_power.hero_id,
            "power_id": new_hero_power.power_id,
            "strength": new_hero_power.strength,
            "hero": {
                "id": new_hero_power.hero.id,
                "name": new_hero_power.hero.name,
                "super_name": new_hero_power.hero.super_name
            },
            "power": {
                "id": new_hero_power.power.id,
                "name": new_hero_power.power.name,
                "description": new_hero_power.power.description
            }
        }

        return make_response(response_data, 201)

    except ValueError as ve:
        return make_response({"errors": [str(ve)]}, 400)

    except Exception as e:
        return make_response({"errors": ["validation errors"]}, 400)



    


















if __name__=='__main__':
    app.run(port=5000, debug=True)


