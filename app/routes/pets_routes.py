"""Routes to API Endpoints"""
from flask import Blueprint, jsonify, current_app
from app.models.model import Pet

# Setup Blueprint
pets_bp = Blueprint('pets', __name__)

@pets_bp.route('/v1/pets', methods=['GET'])
def get_all_pets():

    pets = Pet.query.all()
    current_app.logger.debug("GET Request Received For All Pets")
    return jsonify([pet.serialize() for pet in pets])
