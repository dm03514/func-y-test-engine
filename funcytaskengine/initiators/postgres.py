import psycopg2

from funcytaskengine.initiators.base import BaseInitiator


class SelectInitiator(BaseInitiator):

    def __init__(self, type, query, connection_string):
        self.query = query
        self.conn = psycopg2.connect(connection_string)
        self.query = query

    def execute(self):
        cur = self.conn.cursor()

        results = None

        try:
            cur.execute(self.query)
            results = cur.fetchall()
        finally:
            self.conn.close()
            cur.close()

        return results


class QueryInitiator(BaseInitiator):
    def __init__(self, type, query, connection_string):
        self.query = query
        self.conn = psycopg2.connect(connection_string)
        self.query = query

    def execute(self):
        cur = self.conn.cursor()

        results = None

        try:
            cur.execute(self.query)
            # results = cur.fetchall()
        finally:
            self.conn.commit()
            self.conn.close()
            cur.close()

        return results
