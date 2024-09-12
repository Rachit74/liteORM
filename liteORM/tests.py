import unittest
import sqlite3
from orm import BaseModel

class BaseModelTest(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel('test_database.db')
        # Create a test table
        self.model.execute_query(
            '''
            CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name VARCHAR(20));
            '''
        )
    
    def close_connection(self):
        self.model.connection.close()

    def test_connection(self):
        """
        tests if the connection is being made successfully
        """
        self.assertIsInstance(self.model.connection, sqlite3.Connection)
        self.assertIsInstance(self.model.cursor, sqlite3.Cursor)