# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from urllib.parse import quote_plus


class NewsPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    def __init__(self):
        connection_string = "mongodb://%s:%s@%s%s%s" % (
            quote_plus(settings["MONGODB_USER"]),
            quote_plus(settings["MONGODB_PASS"]),
            settings["MONGODB_URI"],
            settings["MONGODB_DB"],
            "?ssl=true",
        )
        connection = pymongo.MongoClient(connection_string, connect=False)
        db = connection[settings["MONGODB_DB"]]
        self.collection = db[settings["MONGODB_COLLECTION"]]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            print("Headline added to database!")
        return item
