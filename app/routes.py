"""Routes to API Endpoints"""
from flask import Blueprint, request, jsonify, current_app, url_for
from sqlalchemy.exc import IntegrityError
from app.models import db, Owner



# Setup Blueprint
bp = Blueprint('main', __name__)


# CREATE operation, Route to create new owner
@bp.route("/v1/owners/new", methods=["POST"])
def create_owners():

    """
    This endpoint allows for the creation of a new owner record. The owner's
    information must be provided in the request body in JSON format. The required
    field are 'firstName', 'lastName', 'address', 'city', and 'telephone'.

    Param:
    - JSON body with fields:
        - firstName (str): First name of the owner
        - lastName (str): Last name of the owner
        - address (str): Address of owner
        - city (str): City of owner
        - telephone (str): Telephone number of owner (unique)

    Returns:
    - JSON response with the created owner's details.
    - Status code 201 on success
    - Status code 400 if the request data is invalid or telephone number already exists.
    """

    data = request.get_json()
    current_app.logger.debug("POST Request Received To Create Owner")

    firstName = data.get("firstName")
    lastName = data.get("lastName")
    address = data.get("address")
    city = data.get("city")
    telephone = data.get("telephone")

    if not all([firstName, lastName, address, city, telephone]):
        current_app.logger.error("Invalid request data")
        return jsonify({"error": {"code": 400, "message": "Invalid request data"}}), 400


    name = f"{firstName} {lastName}"
    new_owner = Owner(
        name=name,
        address=address,
        city=city,
        telephone=telephone
    )

    try:
        db.session.add(new_owner)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        current_app.logger.error("Telephone number has already exists!")
        return jsonify({
            "error": {
                "code": 400,
                "message": "Telephone number has already exists!"
                }}), 400

    current_app.logger.info("Owner Created Successfully")
    response =  jsonify({"message": "Owner Has Successfully Created!",
                    "data": {
                        "id": new_owner.id,
                        "name": new_owner.name,
                        "address": new_owner.address,
                        "city": new_owner.city,
                        "telephone": new_owner.telephone
                    }})
    response.status_code = 201
    response.headers['Content-Type'] = 'application/json'
    response.headers['Location']= url_for('main.get_owners')
    return response


# READ operation, Route to get all owners
@bp.route("/v1/owners", methods=["GET"])
def get_owners():

    """
    This endpoint retrieves the details of an owner identified by the provided last name.
    If the owner with the specified last name exists, their details along with any 
    associated pets are returned. If the owner does not exist, a 404 error is returned. 
    
    Param:
    - lastName (query parameter, optional): Last name of the owner(s) to filter by.
    
    Returns:
    - JSON response with the owner details and their pets. If lastNmae is provided,
      return the owners with the matching last name; otherwise, returns all owners.
    - Status code 200 on success.
    - Status code 404 if owner not found.  
    """

    lastName = request.args.get("lastName")

    current_app.logger.debug(
        f"GET Request Received For Owners With Last Name: {lastName}")

    if not lastName:

        all_owner = Owner.query.all()
        serialized_owners = [owner.serialize() for owner in all_owner]

        current_app.logger.info("Returning All Owners")
        return jsonify({'data': serialized_owners}), 200

    owners = Owner.query.filter(Owner.name.ilike(f'%{lastName}%')).all()
    if owners:
        matching_owners = [owner.serialize() for owner in owners]
        current_app.logger.info(
            f"Matching Owners Found With The Last Name: {lastName}")
        return jsonify({"data": matching_owners}), 200

    current_app.logger.error(
        f"No Matching Owners Found with The Last Name: {lastName}")
    return jsonify({
                "error": {
                    "code": 404,
                    "message": "Owner Not Found!"}
                    }), 404

# UPDATE operation, Route to update owner's detail
@bp.route("/v1/owners/<int:owner_id>/edit", methods=["PUT"])
def update_owner(owner_id):

    """
    This endpont updates the owner record identified by the given owner ID.
    The request body must be a JSON object containing the fields to be updated:
    name, address, city, and telephone.

    Param:
    - owner_id (path parameter, int): ID of the owner to be updated.
    - JSON body with optional fields:
        - firstName (str): New First name of the owner
        - lastName (str): New Last name of the owner
        - address (str): New Address of owner
        - city (str): New City of owner
        - telephone (str): New Telephone number of owner (unique)
    
    Returns:
    - JSON response with the updated owner's details.
    - Status code 200 on success.
    - Status code 400 if the telephone number already exists.
    - Status code 404 if the owner with the given ID is not found. 
    """

    data = request.get_json()
    owner = Owner.query.get(owner_id)

    if not owner:
        current_app.logger.error(f"No Matching Owners Found with The ID: {owner_id}")
        return jsonify({"error": {
                            "code": 404,
                            "message": "Owner Not Found! Please Enter A Valid ID!"}
                        }), 404

    firstName = data.get('firstName')
    lastName = data.get("lastName")
    name = f'{firstName} {lastName}'

    owner.name = name
    owner.address = data.get('address', owner.address)
    owner.city = data.get('city', owner.city)
    owner.telephone = data.get('telephone', owner.telephone)

    db.session.commit()
    current_app.logger.info("Owner Update Successfully")
    return jsonify({"message": "Owner Detail Updated Successfully!",
                    "data": {
                        "id": owner_id,
                        "name": owner.name,
                        "address": owner.address,
                        "city": owner.city,
                        "telephone": owner.telephone
                    }}), 200
