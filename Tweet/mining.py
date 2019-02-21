import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

# print ("length of the data is: ", len(tweets_data))

tweets = pd.DataFrame()

# print(tweets_data)

tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))

# tweets_by_lang = tweets['lang'].value_counts()
# print(tweets_by_lang)
# fig, ax = plt.subplots()
# ax.tick_params(axis='x', labelsize=15)
# ax.tick_params(axis='y', labelsize=15)
# ax.set_xlabel('Languages', fontsize=15)
# ax.set_ylabel('Number of tweets' , fontsize=15)
# ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
# tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
# plt.show()

import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))

# print (tweets['python'].value_counts()[True])
# print (tweets['javascript'].value_counts()[True])
# print (tweets['ruby'].value_counts()[True])

prg_langs = ['python', 'javascript', 'ruby']
tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# # Setting axis labels and ticks
# ax.set_ylabel('Number of tweets', fontsize=15)
# ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')
# ax.set_xticks([p + 0.1 * width for p in x_pos])
# ax.set_xticklabels(prg_langs)
# plt.grid()
# plt.show()

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

def extract_hashtag(text):
    regex = r'#'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

print(tweets['link'])

a = tweets[tweets.link != '' ].index.tolist()
print(a)
# tweets_relevant = tweets[tweets['relevant'] == True]
# tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

# print (tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'])
# print (tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link'])
# print (tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link'])

tweets['hash_tag'] = tweets['text'].apply(lambda tweet: extract_hashtag(tweet))
print(tweets['hash_tag'])

b = tweets[tweets.hash_tag != '' ].index.tolist()
print(b)