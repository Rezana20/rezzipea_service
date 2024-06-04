import os

import psycopg2
import logging


class DBConnectionManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.conn = psycopg2.connect(os.environ["COCKROACHDB_URL"])
        self.cursor = None

    def open_connection(self):
        self.logger.info('open_connection')
        self.cursor = self.conn.cursor()
        self.logger.info("Connection to CockroachDB open.")
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close_connection(self):
        self.logger.info('close_connection')
        try:
            self.cursor.close()
            self.conn.close()
            self.logger.info("Connection to CockroachDB closed.")
        except Exception as e:
            self.logger.error("Error closing connection:", e)
