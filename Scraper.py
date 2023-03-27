# This code will use the python library 'tweepy' which allows for easy access to the Twitter API. 
#  We will first create an API object and set the authentication credentials. 
#  Then, we will execute a search query to find the top trending tweets and memes for our search terms.
#  Finally, we write the tweet data to a csv.

# Import the necessary libraries
import tweepy
import csv


# Set the authentication credentials
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

# Create new csv_file
with open('DESIRED_FILEPATH+FILENAME', 'w') as csv_file:
  csv_writer = csv.writer(csv_file,dialect='excel')
  header = ['query_number',
            'query',
            'tweet_id',
            'user_id',
            'user_name',
            'user_screen_name',
            'tweet_created_at',
            'tweet_text',
            'truncated',
            'user_location',
            'user.description',
            'user.url',
            'user.entities',
            'user.protected',
            'user.followers_count',
            'user.friends_count',
            'user.created_at',
            'user.favourites_count',
            'user.utc_offset',
            'user.time_zone',
            'user.geo_enabled',
            'user.verified',
            'user.statuses_count',
            'user.contributors_enabled',
            'user.is_translator',
            'user.is_translation_enabled',
            'user.has_extended_profile',
            'user.default_profile',
            'user.default_profile_image',
            'user.following',
            'user.follow_request_sent',
            'user.notifications',
            'user.translator_type',
            'user.withheld_in_countries',
            'tweet._json-screen_name',
            'tweet._json-location',
            'tweet._json-description',
            'tweet._json-url',
            'tweet._json-entities',
            'tweet._json-entities-hashtags', 
            'tweet._json-entities-symbols', 
            'tweet._json-entities-user_mentions', 
            'tweet._json-entities-urls',
            'tweet._json-entities-media',
            'tweet._json-listed_count',
            'tweet._json-lang',
            'tweet._json-is_translator',
            'tweet._json-is_translation_enabled',
            'tweet._json-profile_image_url',
            'tweet._json-profile_image_url_https',
            'tweet._json-default_profile']
  csv_writer.writerow(header)


# Create an API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Accept user input for search terms.
done = False
terms = [] 
i = 0 
while done == False:
  entered_text = input('Enter search term/hashtag/usernames to scrape and hit enter.  When you are done building your list type "done" and hit enter.')
  if entered_text.lower() != 'done':
    i += 1
    current_term = (i, entered_text)
    terms.append(current_term)
  else:
    done = True


with open('DESIRED_FILEPATH+FILENAME', 'a') as csv_file:
  csv_writer = csv.writer(csv_file)
  for term in terms:
    query_number = term[0]
    query = term[1]
    trending_tweets = api.search_full_archive(q=query)
    for tweet in trending_tweets:
      data = [query_number, 
              query, 
              tweet.id,
              tweet.user.id,
              tweet.user.name,
              tweet.user.screen_name,
              tweet.created_at,
              tweet.text,
              tweet._json.get('truncated',''),
              tweet.user.location,
              tweet.user.description,
              tweet.user.url,
              tweet.user.entities,
              tweet.user.protected,
              tweet.user.followers_count,
              tweet.user.friends_count,
              tweet.user.created_at,
              tweet.user.favourites_count,
              tweet.user.utc_offset,
              tweet.user.time_zone,
              tweet.user.geo_enabled,
              tweet.user.verified,
              tweet.user.statuses_count,
              tweet.user.contributors_enabled,
              tweet.user.is_translator,
              tweet.user.is_translation_enabled,
              tweet.user.has_extended_profile,
              tweet.user.default_profile,
              tweet.user.default_profile_image,
              tweet.user.following,
              tweet.user.follow_request_sent,
              tweet.user.notifications,
              tweet.user.translator_type,
              tweet.user.withheld_in_countries,
              tweet._json.get('screen_name',''),
              tweet._json.get('location',''),
              tweet._json.get('description',''),
              tweet._json.get('url',''),
              tweet._json.get('entities',''),
              tweet._json.get('entities','').get('hashtags',''), 
              tweet._json.get('entities','').get('symbols',''), 
              tweet._json.get('entities','').get('user_mentions',''), 
              tweet._json.get('entities','').get('urls',''),
              tweet._json.get('entities','').get('media',''),
              tweet._json.get('listed_count',''),
              tweet._json.get('lang',''),
              tweet._json.get('is_translator',''),
              tweet._json.get('is_translation_enabled',''),
              tweet._json.get('profile_image_url',''),
              tweet._json.get('profile_image_url_https',''),
              tweet._json.get('default_profile','')]
      csv_writer.writerow(data)
      print('done')
