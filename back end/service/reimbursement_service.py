from flask import session
from dao.reimbursement_dao import ReimbursementDao
from model.user import User
from dao.user_dao import UserDao
from exception.invalid_parameter import InvalidParameterError


class ReimbursementService:

    def __init__(self):
        self.reimbursement_dao = ReimbursementDao()
        self.user_dao = UserDao()

    def get_all_reimb_by_user_id(self, user_id, status):
        if status is None:
            return list(map(lambda a: a.to_dict(), self.reimbursement_dao.get_all_reimb_by_user_id(user_id)))

        if status is not None:
            return list(map(lambda a: a.to_dict(), self.reimbursement_dao.get_reimbs_by_id_and_status(user_id, status)))


    def get_all_reimbs(self):
        list_of_reimbs = self.reimbursement_dao.get_all_reimbs()

        list_of_reimb_dictionaries = []
        for reimb_obj in list_of_reimbs:
            list_of_reimb_dictionaries.append(reimb_obj.to_dict())

        return list_of_reimb_dictionaries

    def add_reimb_for_user(self, reimb_object):
        # if not self.reimbursement_dao.add_reimb_for_user(reimb_object):
        #     raise InvalidParameterError()
        return self.reimbursement_dao.add_reimb_for_user(reimb_object).to_dict()

    def update_reimb(self, reimb_object):
        return self.reimbursement_dao.update_reimb(reimb_object).to_dict()

    def get_reimbs_by_status(self, status):
        if status is None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_all_reimbs()))

        if status is not None:
            return list(map(lambda x: x.to_dict(), self.reimbursement_dao.get_reimbs_by_status(status)))


