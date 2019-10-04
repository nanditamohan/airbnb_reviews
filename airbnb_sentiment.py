import pandas as pd
import csv
from textblob import TextBlob

text_reviews = []
date_reviews = []
with open('reviews.csv') as airbnb_reviews: 
    csvReader = csv.reader(airbnb_reviews)
    for row in csvReader: 
        blob = TextBlob(row[1])
        if(blob.detect_language() != 'en'): 
            blob = blob.translate(from_lang=blob.detect_language(), to='en')
        print(blob)
        print(blob.sentiment.polarity)
        text_reviews.append(blob.sentiment.polarity)
        date_reviews.append(row[0])


