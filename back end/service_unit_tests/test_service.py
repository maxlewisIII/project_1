
from model.reimbursement import Reimbursement
from service.reimbursement_service import ReimbursementService
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

# def test_login(mocker):



