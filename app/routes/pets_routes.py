"""Routes to API Endpoints"""
from flask import Blueprint, jsonify, current_app
from app.models.model import Pet

# Setup Blueprint
pets_bp = Blueprint('pets', __name__)

@pets_bp.route('/v1/pets', methods=['GET'])
def get_all_pets():
    """
    This endpoint retrieves the details of all pets from the database.

    Returns:
    - JSON response with all pets details. 
    - Status code 200 on success.
    """
    current_app.logger.debug("GET Request Received For All Pets")
    pets = Pet.query.all()
    serialized_pets = [pet.serialize() for pet in pets]

    current_app.logger.debug("GET Request Received For All Pets")
    return jsonify({"data": serialized_pets}), 200
