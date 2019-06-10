import pymongo
from pymongo import MongoClient


class RegisterModel:
    @staticmethod
    def insert_user(data):
        print("Data is :", data)
