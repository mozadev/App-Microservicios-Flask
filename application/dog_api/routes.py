from . import dog_api_blueprint
from .. import db
from ..models import Dog
from flask import request, jsonify

@dog_api_blueprint.route('/api/dogs',  methods=['GET'])
def dogs():
    dogs = []
    for row in Dog.query.all():
        dogs.append(row.to_json())
        
    response = jsonify({'results': dogs})
    return response


@dog_api_blueprint.route('/api/dog/add', methods=['POST'])
def add_dog():
     name = request.form['name']
     color = request.form['color']
     size = request.form['size']
     age = request.form['age']
     gender = request.form['gender']
     breed = request.form['breed']
     
     
     dog = Dog()
     dog.name = name
     dog.color = color
     dog.size = size
     dog.age = age
     dog.gender = gender
     dog.breed = breed
     
     db.session.add(dog)
     db.session.commit()
     
     response = jsonify({'message': 'Dog added', 'dog' : dog.to_json()})
     return response
 
 
 
@dog_api_blueprint.route('/api/dog/update/<int:id>', methods=['PUT'])
def update_dog(id):
     #search dgo by id
     dog = Dog.query.get(id)
     if dog is None:
         # Si no encuentra el perro, return a error message
         response = jsonify({'message': 'Dog not found'})
         response.status_code = 404
         return response
     #update attributes of the dog with the date given
     #here we use request.json instead of request.form because PUT used  sending date on format a json object
     data = request.json
     dog.name = data.get('name', dog.name)
     dog.color = data.get('color', dog.color)
     dog.size = data.get('size', dog.size)
     dog.age = data.get('age', dog.age)
     dog.gender = data.get('gender', dog.gender)
     dog.breed = data.get('breed', dog.breed)
     
     # Save the changes on the database
     db.session.commit()
     
     # Return a respons indicando the success of the operation
     response = jsonify({'message': 'Dog updated', 'dog':dog.to_json()})
     return response 
 
 
@dog_api_blueprint.route('/api/dogs/<int:dog_id>', methods = ['GET'])
def get_dog(dog_id):
    #Search the dog by id
    dog = Dog.query.get(dog_id)
    if dog:
        # If founded the dog, return the date of the dog
        response = jsonify(dog.to_json())
    else:
        # if not founded the dog, return a error message
        response = jsonify({'message': 'Dog not found'})
        response.status_code = 404
    return response



@dog_api_blueprint.route('/api/dog/<int:dog_id>', methods = ['DELETE'])
def delete_dog(dog_id):
    #Search the dog by id
    dog = Dog.query.get(dog_id)
    if dog is None:
        # If not founded the dog, return a error message
        response = jsonify({'message': 'Dog not found'})
        response.status_code = 404
        return response
    #Delete the dog from the database
    db.session.delete(dog)
    db.session.commit()
    # Return a response indicating the success of the operation
    response = jsonify({'message': 'Dog deleted'})
    response.status_code = 200
    return response



 
 
 
 
     


     
     
     
     
     
