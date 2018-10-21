import pymongo
import flask_config
from urllib.parse import quote_plus
from bson.json_util import dumps


def get_collection():
    connection_string = "mongodb://%s:%s@%s%s%s" % (
        quote_plus(flask_config.mongo_username),
        quote_plus(flask_config.mongo_password),
        flask_config.mongo_uri,
        flask_config.mongo_database,
        "?ssl=true",
    )
    connection = pymongo.MongoClient(connection_string, connect=False)
    db = connection[flask_config.mongo_database]
    return db[flask_config.mongo_collection]


def find_intext(search_term):
    collection = get_collection()
    results = collection.find({"$text": {"$search": search_term}}).limit(10)
    return dumps(results)
