
import tweepy
import re
import nltk
import math
import spacy
from nltk.corpus import stopwords
from transformers import T5Tokenizer, T5ForConditionalGeneration
from datetime import datetime, timedelta


# set up Twitter API credentials
consumer_key = "skakU2irbEBd97RvhpBsW0sXL"
consumer_secret = "Bgb8TuOlhCB0nRBpyJCMtKOLkvhuSW7D0V1EoJzf7p7McFwknf"
access_token = "880363396016869376-fFRlVcD2l7sMDmpGZw3yZelKxijcwEP"
access_token_secret = "l0QpT9WuWXHCV4on1C20irIzXYrtxIoHoJXHtSh7vxG4j"


# set up API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# set up API client
api = tweepy.API(auth)

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

nlp = spacy.load('en_core_web_sm')


def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # remove urls
    text = re.sub(r'\#\w+\rt', '', text)  # remove hashtags
    text = text.lower()  # convert to lowercase
    text = ' '.join([word for word in text.split() if word not in stop_words])  # remove stop words
    return text
    


# Extract relevant tweets based on keywords and dates
start_date = datetime.now() - timedelta(days=5)
end_date = datetime.now()

# Collect tweets for each day
for i in range((end_date - start_date).days):
    day = start_date + timedelta(days=i)
    date_str = day.strftime("%Y-%m-%d")
    
    # Extract relevant tweets based on keywords
    keywords = ['earthquake']
    tweets = []
    primary_locations={'testing':0}
    location_summaries={}
    for keyword in keywords:
        for tweet in tweepy.Cursor(api.search, q=keyword, lang='en', tweet_mode='extended', until=date_str).items(100):
            text = tweet.full_text
            preprocessed_text = preprocess_text(text)
            tweets.append(preprocessed_text)
            
            # Extract location entities from tweet text
            doc = nlp(preprocessed_text)
            locations = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
            
            if len(locations)>1:
              locations=[locations[0]]

            for location in locations:
              if location not in primary_locations:
                primary_locations[location]=0
              else:
                primary_locations[location]=primary_locations[location]+1

              if location not in location_summaries:
                location_summaries[location] = []
              location_summaries[location].append(preprocessed_text)
            
    print(primary_locations)
    #print(primary_locations.values())
    max_value = max(primary_locations.values())
    #print(max_value) 

    threshold=math.floor(math.sqrt(max_value))

    # Rank and summarize the relevant tweets using a machine learning-based model (T5)
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    model = T5ForConditionalGeneration.from_pretrained('t5-base')
    
    #prev_sum="";
    print()
    print()
    print("#"*20)
    print(f"Summary for {date_str}:")
    print("#"*20)
    for location, location_tweets in location_summaries.items():
        if primary_locations[location]>=threshold:
          input_text = ' '.join(location_tweets)
          input_ids = tokenizer.encode(input_text, return_tensors='pt')
          summary_ids = model.generate(input_ids, num_beams=4, length_penalty=2.0, max_length=100, min_length=10, no_repeat_ngram_size=2)
          summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
          #if prev_sum != summary:
          print(f"Summaries for {location}:")
          # Output summary for each location
          print(summary)
          print()
          #prev_sum=summary

     