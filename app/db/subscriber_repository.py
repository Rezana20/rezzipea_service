from __future__ import annotations
import logging

from rezzipea_service.app.db.db_connection_manager import DBConnectionManager


class SubscriberRepository:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.connection_manager = DBConnectionManager()

    def __is_subscriber_email_unique(self, email: str, cursor: any) -> bool:
        """
        Checks if the given email is unique among existing subscribers.

        This method queries the database to check if there is any existing subscriber
        with the given email.

        Parameters:
        email (str): The email address to check for uniqueness.

        Returns:
        bool: True if the email is unique (no existing subscriber with that email),
            False otherwise.
        """
        self.logger.info("is_subscriber_email_unique")
        try:

            find_subscribers = ("SELECT * FROM subscriber WHERE email = %s")
            cursor.execute(find_subscribers, (email,))

            self.logger.info("Query find_subscriber executed successfully")

            result = cursor.fetchone()

            if result is None:
                self.logger.info("No existing subscriber found. The subscriber can be added.")
                return True
            else:
                result_value = result[0]  # Access the first column of the result
                self.logger.info("Subscriber already exists: %s", result_value)
                return False
                
        except Exception as e:
            self.logger.error("Error checking if a subscriber is unique: %s", e)

    def get_all_subscribers(self) -> list:
        """
        Retrieves all subscribers from the database.

        This method executes a SQL query to fetch all records from the `subscriber`
        table. It logs the execution of the query and returns the result set.
        If an exception occurs during the execution of the query, it logs the error
        and returns an empty list.

        Returns:
        List: A list of all subscriber records retrieved from the database. Each
          record is represented as a tuple. Returns an empty list if no records
          are found or if an error occurs.
        """
        self.logger.info("get_all_subscribers")
        try:
            cursor = self.connection_manager.open_connection()

            select_all_subscribers = ("SELECT * FROM subscriber")
            cursor.execute(select_all_subscribers)

            self.logger.info("Query select_all_subscribers executed successfully")

            result = cursor.fetchall()
            
            self.connection_manager.close_connection()

            return result

        except Exception as e:
            self.logger.error("Error executing query: %s", e)
            return []

    def add_subscriber(self, email: str, name: str) -> str | None:
        """
        Adds a new subscriber to the database.

        This method first checks if the email is unique among subscribers. If the email
        is unique, it inserts a new record into the `subscriber` table with the provided
        email and name. It then logs the successful insertion and returns the result.
        If the email is not unique, it logs a message and returns None.
        If an exception occurs during the process, it logs the error and returns None.

        Parameters:
        email (str): The email address of the new subscriber.
        name (str): The name of the new subscriber.

        Returns:
        str | None: The newly added record  of the subscriber if successful, None otherwise.
        """
        self.logger.info("add_subscriber")
        try:
            cursor = self.connection_manager.open_connection()
            if self.__is_subscriber_email_unique(email, cursor):

                # Todo consider fetching the id of the record.
                insert_subscriber = ("INSERT INTO subscriber(email, name) VALUES (%s, %s)")
                cursor.execute(insert_subscriber, (email, name))

                self.logger.info("Query insert_subscriber executed successfully")
                result = cursor.fetchone()

                self.connection_manager.close_connection()
                if result is not None:
                    result_value = result[0]
                    self.logger.info("Subscriber added: %s",result_value)
                    return result_value
                    # Todo send welcome email
            else:
                self.logger.info("Cannot add subscriber with that email: %s", email)
                return None

        except Exception as e:
            # Todo, let the user know something went wrong and
            #  send alert to OE list with details to manually add user.
            self.logger.error("Error executing insert new subscriber: %s", e)
            return None

    