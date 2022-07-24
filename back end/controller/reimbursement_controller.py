from flask import Blueprint, request, session
from model.user import User
from model.reimbursement import Reimbursement
from service.reimbursement_service import ReimbursementService
from exception.invalid_parameter import InvalidParameterError
from service.reimbursement_service import ReimbursementService


rc = Blueprint('reimbursement_controller', __name__)

reimbursement_service = ReimbursementService()


@rc.route("/users/<user_id>/reimbursements")   # GET /users/<user_id>
def get_all_reimb_by_user_id(user_id):
    args = request.args
    status = args.get('status')
    return {"reimbursements": reimbursement_service.get_all_reimb_by_user_id(user_id)}

@rc.route("/reimbursements")
def get_all_reimbs():
    return {
        "reimbursements": reimbursement_service.get_all_reimbs()
    }

@rc.route("/users/<user_id>/reimbursements", methods=["POST"])
def add_reimb_for_user(user_id):
    new_reimb = request.get_json()
    reimb_object = Reimbursement(None, new_reimb['reimb_amount'], None, None, None, new_reimb['type'],
                                 new_reimb['description'], None, user_id, None)

    try:
        return reimbursement_service.add_reimb_for_user(reimb_object), 201
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400