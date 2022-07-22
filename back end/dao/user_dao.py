import psycopg

from model.user import User


class UserDao:

    def get_user_by_username(self, username):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE username = %s", (username,))

                user_info = cur.fetchone()

                if user_info is None:
                    return None

                username = user_info[0]
                password = user_info[1]
                first_name = user_info[2]
                last_name = user_info[3]
                gender = user_info[4]
                phone_number = user_info[5]
                email_address = user_info[6]

                return User(username, password, first_name, last_name, gender, phone_number, email_address)

    def get_user_by_username_and_password(self, username, password):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from users WHERE username = %s AND password = %s", (username, password))

                user_info = cur.fetchone()

                if user_info is None:
                    return None

                username = user_info[0]
                password = user_info[1]
                first_name = user_info[2]
                last_name = user_info[3]
                gender = user_info[4]
                phone_number = user_info[5]
                email_address = user_info[6]

                return User(username, password, first_name, last_name, gender, phone_number, email_address)

    def get_user_by_email(self, email):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from users WHERE email_address = %s", (email,))

                user_info = cur.fetchone()

                if user_info is None:
                    return None

                username = user_info[0]
                password = user_info[1]
                first_name = user_info[2]
                last_name = user_info[3]
                gender = user_info[4]
                phone_number = user_info[5]
                email_address = user_info[6]

                return User(username, password, first_name, last_name, gender, phone_number, email_address)

    def add_user(self, user_obj):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="1234") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *",
                            (user_obj.user_id,
                             user_obj.username,
                             user_obj.password,
                             user_obj.first_name,
                             user_obj.last_name,
                             user_obj.email_address,
                             user_obj.role))

                user_that_was_inserted = cur.fetchone()
                conn.commit()

                return User(user_that_was_inserted[0], user_that_was_inserted[1], user_that_was_inserted[2]
                            , user_that_was_inserted[3], user_that_was_inserted[4], user_that_was_inserted[5], user_that_was_inserted[6])
