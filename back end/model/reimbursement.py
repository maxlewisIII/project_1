class Reimbursement:
    def __init__(self, reimb_id, reimbursement_amount, submission_date,
                 resolved_date, status, type, description, receipt, reimb_author, reimb_resolver):
        self.reimb_id = reimb_id
        self.reimbursement_amount = reimbursement_amount
        self.submission_date = submission_date
        self.resolved_date = resolved_date
        self.status = status
        self.type = type
        self.description = description
        self.receipt = receipt
        self.reimb_author = reimb_author
        self.reimb_resolver = reimb_resolver

    def to_dict(self):
        return {
            'reimb_id': self.reimb_id,
            'reimbursement_amount': self.reimbursement_amount,
            'submission_date': self.submission_date,
            'resolved_date': self.resolved_date,
            'status': self.status,
            'type': self.type,
            'description': self.description,
            'receipt' : self.receipt,
            'reimb_author': self.reimb_author,
            'reimb_resolver': self.reimb_resolver,
        }

# r1 = Reimbursement(1, 1000, '', '', 'pending', 'travel', 'hotel', '', '1', '')
# print(r1.to_dict())
