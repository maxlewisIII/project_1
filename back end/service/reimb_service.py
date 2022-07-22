from flask import session
from dao.reimb_dao import ReimbursementDao
# from exceptions.incorrect_user_error import IncorrectUserError
from model.user import User
from dao.user_dao import UserDao


class ReimbursementService:

    def __init__(self):
        self.reimbursement_dao = ReimbursementDao()
        self.user_dao = UserDao()

    def get_all_reimb_by_user_id(self, user_id):
        return list(map(lambda a: a.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id(user_id)))

    def get_all_reimbs(self):
        list_of_reimbs = self.reimbursement_dao.get_all_reimbs()

        list_of_reimb_dictionaries = []
        for reimb_obj in list_of_reimbs:
            list_of_reimb_dictionaries.append(reimb_obj.to_dict())

        return list_of_reimb_dictionaries



