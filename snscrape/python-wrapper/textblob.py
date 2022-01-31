# from textblob import TextBlob
# import pandas as pd
# Input_file='data tiap tahun dari 2020_2022.xlsx'
# df = pd.read_excel(Input_file, sheet_name='2021')
# col1 = pd['tweet_id'].tolist()
# col2 = pd['description'].tolist()
# blob = TextBlob(col1)
# blob1 = Texxtblob(col2)
# polarity_score = blob.sentiment.polarity
# polarity_rounded = round(polarity_score, 6)
# print(polarity_rounded)
import pandas as pd

# To read a CSV file
df = pd.read_csv('./text-query-tweets-v2.csv')
df = pd.DataFrame({'text'})

from textblob import TextBlob

# The x in the lambda function is a row (because I set axis=1)
# Apply iterates the function accross the dataframe's rows
df['polarity'] = df.apply(lambda x: TextBlob(x['sentence']).sentiment.polarity, axis=1)
df['subjectivity'] = df.apply(lambda x: TextBlob(x['sentence']).sentiment.subjectivity, axis=1)
print(df)