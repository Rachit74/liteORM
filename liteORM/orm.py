import sqlite3

"""
class BaseModel

Base Model class starts a new connection with the database and provide basic queries to run
"""
class BaseModel:
    def __init__(self, db_name):
        """
        Makes the connection
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    # def execute_query(self, query, params=()):
    #     """
    #     function to execute to query with parms
    #     """
    #     self.cursor.execute(query, params)
    #     self.connection.commit()

    # def fetch_query(self, query, params=()):
    #     """
    #     function to execute to a query with params and fetch the records
    #     """
    #     self.cursor.execute(query, params)
    #     return self.cursor.fetchall()
