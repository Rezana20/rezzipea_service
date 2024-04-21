import os
import psycopg2


class CockroachDBConnection:
    def __init__(self):
        self.conn = psycopg2.connect(os.environ["COCKROACHDB_URL"])
        self.cursor = self.conn.cursor()

    def is_subscriber_email_unique(self, email: str):
        try:
            print(email)
            find_subscribers = ("SELECT * FROM subscriber WHERE email = %s")
            self.cursor.execute(find_subscribers, (email,))
            print("Query find_subscriber executed successfully")
            result = self.cursor.fetchone()

            if result is not None:
                result_value = result[0]  # Access the first column of the result
                print("User found", result_value)
                self.close_connection()
                return False
            else:
                print("No result found, you will want to add the subscriber")
                self.close_connection()
                return True
        except Exception as e:
            print("Error executing query:", e)

    def get_all_subscribers(self):
        try:
            select_all_subscribers = ("SELECT * FROM subscriber")
            self.cursor.execute(select_all_subscribers)
            print("Query select_all_subscribers executed successfully")
            result = self.cursor.fetchall()
            self.close_connection()
            return result
        except Exception as e:
            print("Error executing query:", e)

    def close_connection(self):
        try:
            self.cursor.close()
            self.conn.close()
            print("Connection to CockroachDB closed")
        except Exception as e:
            print("Error closing connection:", e)
