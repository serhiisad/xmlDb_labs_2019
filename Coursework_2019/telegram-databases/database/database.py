from pymongo import MongoClient
import os

def connect(db_name="course-work"):
    # client = MongoClient("localhost:27017")
    client = MongoClient("localhost:27100")
    return client[db_name]


def export_collection(db_name="course-work", collection="messages", filepath="backup/messages.json", host="localhost:27100"):
    command = "mongoexport --db {} --collection {} --out {} --host {}".format(db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} exported to file {}".format(db_name, collection, filepath)


def import_collection(db_name="course-work", collection="messages", filepath="backup/messages.json", host="localhost:27100"):
    command = "mongoimport --db {} --collection {} --file {} --host {}".format(db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} imported to file {}".format(db_name, collection, filepath)