import config

ITEM_PIPELINES = {"news.pipelines.MongoDBPipeline": 300}
mongo_uri = "portal-ssl809-1.rational-mongodb-25.2578074201.composedb.com:16787/"
mongo_username = config.username
mongo_password = config.password
mongo_database = "theguardian"
mongo_collection = "articles"
