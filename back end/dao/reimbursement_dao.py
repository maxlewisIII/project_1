import psycopg
from model.reimbursement import Reimbursement
from model.user import User


class ReimbursementDao:

    def get_all_reimb_by_user_id(self, reimb_author):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="postgres", user="postgres",
                             password='1234') as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursement WHERE reimb_author = %s", (reimb_author,))

                my_list_of_reimbursement_objs = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    author = reimb[8]
                    resolver = reimb[9]

                    my_reimb_obj = Reimbursement(reimb_id, amount, submitted, resolved, status, type, description,
                                                 receipt, author, resolver)
                    my_list_of_reimbursement_objs.append(my_reimb_obj)

                return my_list_of_reimbursement_objs

    def get_all_reimbs(self):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursement")

                my_list_of_reimbursements = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    reimb_amount = reimb[1]
                    submission_date = reimb[2]
                    resolved_date = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    reimb_author = reimb[8]
                    reimb_resolver = reimb[9]


                    my_reimb_obj = Reimbursement(reimb_id, reimb_amount, submission_date, resolved_date, status,
                                            type, description, receipt, reimb_author, reimb_resolver)
                    my_list_of_reimbursements.append(my_reimb_obj)

                return my_list_of_reimbursements

    def add_reimb_for_user(self, reimb_object):

        amount_to_add = reimb_object.reimb_amount
        type_to_add = reimb_object.type
        description_to_add = reimb_object.description
        user_id_to_add = reimb_object.reimb_author
        date_to_add = reimb_object.submission_date
        receipt_to_add = reimb_object.receipt

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="1234") as conn:

            with conn.cursor() as cur:
                cur.execute("INSERT INTO reimbursement (reimb_amount, type, description, reimb_author, submission_date) VALUES (%s, %s, %s, %s, %s) RETURNING *",
                            (amount_to_add, type_to_add, description_to_add, user_id_to_add, date_to_add))

                reimb_row = cur.fetchone()

                conn.commit()

                return Reimbursement(reimb_row[0], reimb_row[1], reimb_row[2], reimb_row[3], reimb_row[4],
                                     reimb_row[5], reimb_row[6], reimb_row[7], reimb_row[8], reimb_row[9])

    def update_reimb(self, reimb_object):
        with psycopg.connect(host="127.0.0.1", port='5432', dbname="postgres", user="postgres",
                             password='1234') as conn:
            with conn.cursor() as cur:
                cur.execute('UPDATE reimbursement SET status = %s, reimb_resolver = %s, resolved_date = CURRENT_TIMESTAMP'
                            ' WHERE reimb_id = %s RETURNING *',
                            (reimb_object.status, reimb_object.reimb_resolver, reimb_object.reimb_id))

                conn.commit()

                updated_reimb = cur.fetchone()
                if updated_reimb is None:
                    return None

                return Reimbursement(updated_reimb[0], updated_reimb[1], updated_reimb[2], updated_reimb[3],
                                     updated_reimb[4], updated_reimb[5], updated_reimb[6], updated_reimb[7],
                                     updated_reimb[8], updated_reimb[9])

    def get_reimbs_by_status(self, status):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursement WHERE status = %s", (status,))

                my_list_of_reimbursements = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    reimb_amount = reimb[1]
                    submission_date = reimb[2]
                    resolved_date = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    reimb_author = reimb[8]
                    reimb_resolver = reimb[9]


                    my_reimb_obj = Reimbursement(reimb_id, reimb_amount, submission_date, resolved_date, status,
                                            type, description, receipt, reimb_author, reimb_resolver)
                    my_list_of_reimbursements.append(my_reimb_obj)

                return my_list_of_reimbursements

    def get_reimbs_by_id_and_status(self, user_id, status):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM reimbursement WHERE reimb_author = %s AND status = %s", (user_id, status))

                my_list_of_reimbursements = []

                for reimb in cur:
                    reimb_id = reimb[0]
                    reimb_amount = reimb[1]
                    submission_date = reimb[2]
                    resolved_date = reimb[3]
                    status = reimb[4]
                    type = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    reimb_author = reimb[8]
                    reimb_resolver = reimb[9]


                    my_reimb_obj = Reimbursement(reimb_id, reimb_amount, submission_date, resolved_date, status,
                                            type, description, receipt, reimb_author, reimb_resolver)
                    my_list_of_reimbursements.append(my_reimb_obj)

                return my_list_of_reimbursements






