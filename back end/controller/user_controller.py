from flask import Blueprint, request, session

from exception.login import LoginError
from exception.registration import RegistrationError
from model.user import User
from service.user_service import UserService

uc = Blueprint("user_controller", __name__)
user_service = UserService()

@uc.route('/login', methods=['POST'])
def login():

    request_body_dict = request.get_json()


    username = request_body_dict.get('username')
    password = request_body_dict.get('password')

    # print("test")


    try:
        user_dict = user_service.login(username, password)

        session['user_info'] = user_dict

        return user_dict, 200
    except LoginError as e:
        return {
            "message": str(e)
        }, 400

@uc.route('/logout', methods=['POST'])
def logout():
    session.clear()

    return {
        "message": "Successfully logged out"
    }, 200, session.clear()


@uc.route('/loginstatus', methods=['GET'])
def loginstatus():
    if session.get('user_info') is not None:
        return {
            "message": "You are logged in",
            "logged in user": session.get('user_info')
        }, 200
    else:
        return {
            "message": "You are not logged in"
        }, 200


@uc.route('/users', methods=['POST'])
def add_user():
    request_body_dict = request.get_json()

    user_id = request_body_dict.get('user_id')
    username = request_body_dict.get('username')
    password = request_body_dict.get('password')
    first_name = request_body_dict.get('first_name')
    last_name = request_body_dict.get('last_name')
    email_address = request_body_dict.get('email_address')
    role = request_body_dict.get('role')

    try:
        added_user = user_service.add_user(User(user_id, username, password, first_name, last_name, email_address, role))

    except RegistrationError as e:
        return {
            "messages": e.messages
        }, 400

    return added_user, 201



