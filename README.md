# webscraper-coding-challenge

This was written as part of a coding challenge to store sanitised webscraping results into a mongo database accessable via API

# Instructions 
1. Start a virtualenv environment and install requirements.txt
2. Create a config file in the news directory with the username and password for the database
3. Navigate to the news directory and intitiate the webcrawler with scrapy crawl news
4. Once the spider has finished putting the results into the mongodb database initiate the flask api by running api.py
5. Results will now be available via the API

# Using the API
Simply post json in the following format {"searchterm": "sea cucumber example text"} in a post request to the /intext endpoint with your search terms to search accross all text fields in the database
the result will be in JSON format
