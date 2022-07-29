from service.user_service import UserService
from model.reimbursement import Reimbursement
from service.reimbursement_service import ReimbursementService
from exception.login import LoginError
from model.user import User
import pytest


def test_get_all_reimbs(mocker):
    def mock_get_all_reimbs(self):
        return[Reimbursement(1, 100, None, None, 'pending', 'travel', 'hotel', None, 1, 3),
               Reimbursement(2, 100, None, None, 'denied', 'food', 'lunch', None, 1, 3)]

    mocker.patch('dao.reimbursement_dao.ReimbursementDao.get_all_reimbs', mock_get_all_reimbs)

    reimbursement_service = ReimbursementService()

    actual = reimbursement_service.get_all_reimbs()

    assert actual == [
        {
            "reimb_id": 1,
            "reimb_amount": 100,
            "submission_date": None,
            "resolved_date": None,
            "status": "pending",
            "type": "travel",
            "description": "hotel",
            "receipt": None,
            "reimb_author": 1,
            "reimb_resolver": 3
        },
        {
            "reimb_id": 2,
            "reimb_amount": 100,
            "submission_date": None,
            "resolved_date": None,
            "status": "denied",
            "type": "food",
            "description": "lunch",
            "receipt": None,
            "reimb_author": 1,
            "reimb_resolver": 3
        }
    ]

def test_login_positive(mocker):
    def mock_login(self, username, password):
        if username == 'johndoe' and password == 'pass123$':
            return (User(1, 'johndoe', 'pass123$', 'John', 'Doe', 'johndoe@gmail.com', 'employee'))
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_username_and_password', mock_login)

    user_service = UserService()

    actual = user_service.login("johndoe", "pass123$")

    assert actual == {
            "user_id": 1,
            "username": "johndoe",
            "password": "pass123$",
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "johndoe@gmail.com",
            "role": "employee"
        }

def test_login_negative(mocker):
    def mock_login(self, username, password):
        if username == 'johndoee' and password == 'pass123$':
            return (User(1, 'johndoe', 'pass123$', 'John', 'Doe', 'johndoe@gmail.com', 'employee'))
        else:
            return None

    mocker.patch('dao.user_dao.UserDao.get_user_by_username_and_password', mock_login)

    user_service = UserService()


    try:
        actual = user_service.login("johndoe", "pass123$")

        assert False

    except LoginError:
        assert True

def test_add_user(mocker, user_obj_to_add=None):
    def mock_add_user(self,user_obj):
        if user_obj == user_obj_to_add:
            return User(None, 'johndoe', 'password', 'John', 'Doe', 'johndoe@gmail.com', 'employee')
        else:
            return None
    mocker.patch('dao.user_dao.UserDao.add_user', mock_add_user)
    user_service = UserService()
    actual = user_service.add_user(user_obj_to_add)
    assert actual == {
            "user_id": None,
            "username": "johndoe",
            "password": "password",
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "johndoe@gmail.com",
            "role": "employee"
    }















