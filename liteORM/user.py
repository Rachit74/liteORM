# importing orm.py for BaseModel
from orm import BaseModel

class User(BaseModel):
    def __init__(self, db_name):
        super().__init__(db_name=db_name)
        self.create_table()

    def create_table(self):
        create_user_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
            id INTERGER PRIMARY KEY AUTO INCREMENT,
            username VARCHAR(20)
            );
        '''
        self.execute_query(create_user_table_query)

    """
    orm.save() method to save the details of the current instance of user object
    """
    def save(self, username):
        self.username = username
    
    """
    orm.commit() method to commit the details of the current instance of user object to the DB table
    """
    def commit(self):
        commit_user_query = 'INSERT INTO users (name) VALUES (?)'
        self.execute_query(query=commit_user_query, params=(self.username))

    """
    orm.get_all_users() to fetch records of all the users
    """
    def get_all_users(self):
        get_all_users_query = 'SELECT * FROM users'
        return self.fetch_query(query=get_all_users_query)