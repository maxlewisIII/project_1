import psycopg

from model.user import User


class UserDao:

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
