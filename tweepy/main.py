import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Step 1: Authenticate with the Twitter API
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Step 2: Search for Tweets
search_term = 'Python'  # Example search term
public_tweets = api.search(q=search_term, count=100, lang='en', tweet_mode='extended')

# Step 3: Analyze Sentiment and store results
# Create empty lists to store sentiment and tweet timestamps
sentiments = []
tweet_times = []

for tweet in public_tweets:
    # Extract the full text of the tweet
    tweet_text = tweet.full_text
    
    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(tweet_text)
    
    # Get the polarity score
    sentiment = analysis.sentiment.polarity
    
    # Store sentiment and timestamp in the lists
    sentiments.append(sentiment)
    tweet_times.append(tweet.created_at)

# Step 4: Convert to a DataFrame for easier plotting
data = pd.DataFrame({'Time': tweet_times, 'Sentiment': sentiments})

# Step 5: Sort the DataFrame by time (in case tweets are out of order)
data = data.sort_values(by='Time')

# Step 6: Plotting the sentiment trend over time
plt.figure(figsize=(10,6))
sns.lineplot(x='Time', y='Sentiment', data=data)
plt.title(f"Sentiment Trend for '{search_term}' Over Time")
plt.xlabel('Time')
plt.ylabel('Sentiment (Polarity)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
