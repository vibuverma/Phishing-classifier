import shutil
import sqlite3
from os import listdir 
import os
import csv
from application_logging.logger import App_Logger

class dBOperations:
    """
        This class shall be used for handling all the SQL operations.

    """
    def __init__(self):
        self.path= 'Prediction_Database/'
        self.badFilePath = 'Prediction_Raw_Files_validated/Bad_Raw'
        self.goodFilePath = 'Prediction_Raw_Files_validated/Good_Raw'
        self.logger = App_Logger()

    def dataBaseConnection(self, DatabaseName):
        """
            Method Name: dataBaseConnection
            Description: This method creates the database with the given name and if already exists then opens the connection to the DB.
            Output: Connection to the DB.
            On Failure: Raise ConnectionError.
        """
        pass