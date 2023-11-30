# data_manager.py
# Handles data storage, retrieval, and management using SQLite

import sqlite3
from sqlite3 import Error

class DataManager:
    def __init__(self, db_file):
        """ Initialize the DataManager with a database file """
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """ Create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, create_table_sql):
        """ Create a table from the create_table_sql statement """
        try:
            c = self.connection.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def store_data(self, table, data):
        """
        Store data in the table
        :param table: Table name
        :param data: Data to be inserted as a dictionary
        """
        columns = ', '.join(data.keys())
        placeholders = ':'+', :'.join(data.keys())
        sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, data)
            self.connection.commit()
        except Error as e:
            print(e)

    def retrieve_data(self, table, query_conditions):
        """
        Retrieve data from the table
        :param table: Table name
        :param query_conditions: Conditions for the query
        :return: Fetched data
        """
        sql = f'SELECT * FROM {table} WHERE {query_conditions}'
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(e)
            return []

# Example usage
if __name__ == '__main__':
    database = "example.db"

    data_manager = DataManager(database)

    # Define SQL for creating a table
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        start_date text,
                                        end_date text
                                    ); """

    data_manager.create_table(sql_create_projects_table)

    # Example data insertion
    project_data = {'name': 'Example Project', 'start_date': '2021-01-01', 'end_date': '2021-12-31'}
    data_manager.store_data('projects', project_data)

    # Example data retrieval
    projects = data_manager.retrieve_data('projects', 'name="Example Project"')
    print(projects)
