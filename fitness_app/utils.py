from pymongo import MongoClient
from django.conf import settings

def get_db_connection():
    client = MongoClient(
        host=settings.MONGO_DB['HOST'],
        port=settings.MONGO_DB['PORT']
    )
    return client[settings.MONGO_DB['NAME']]