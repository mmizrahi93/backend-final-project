from flask import Blueprint, jsonify, request
from flask_login import current_user
import models

from playhouse.shortcuts import model_to_dict
from peewee import IntegrityError

show = Blueprint('shows', 'show')

@show.route('/', methods=["POST"])
def create_show():
    payload = request.get_json()
    print(payload)
    try:
        show = models.Show.create(name=payload['name'], type=payload['type'], category=payload['category'], where=payload['where'])

        print(show.__dict__)

        return jsonify(data=model_to_dict(show), status={'code': 201, 'message': 'Success'})
    except IntegrityError as err:
        print('Invalid Schema was sent')
        print(err)
        return jsonify(data={}, status={'code': 401, 'message': 'Invalid show schema'})

#  show route
@show.route('/<id>', methods=["GET"])
def get_one_show(id):
    show = models.Show.get_by_id(id)
    print(show.__dict__)
    return jsonify(data=model_to_dict(show), status={"code": 200, "message": "Success"})

# update route
@show.route('/<id>', methods=["PUT"])
def update_show(id):
    payload = request.get_json()
    query = models.Show.update(**payload).where(models.Show.id==id)
    query.execute()
    return jsonify(data=model_to_dict(models.Show.get_by_id(id)), status={"code": 200, "message": "resource updated successfully"})

# delete route
@show.route('/<id>', methods=["Delete"])
def delete_show(id):
    query = models.Show.delete().where(models.Show.id==id)
    query.execute()
    return jsonify(data='show successfully deleted', status={"code": 200, "message": "resource deleted successfully"})

# get route
@show.route('/', methods=["GET"])
def get_all_shows():
    try:
        db_shows = models.Show.select()
        shows = []

        for show in db_shows:
            print(show)
            print(model_to_dict(show))
            shows.append(model_to_dict(show))

        return jsonify(data=shows, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})