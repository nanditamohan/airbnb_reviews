import pandas as pd
import csv
from textblob import TextBlob

# text_reviews = []
date_reviews = []
with open('complete_reviews.csv') as airbnb_reviews: 
    csvReader = csv.reader(airbnb_reviews)
    csv_data = [[]]
    writer = csv.writer(airbnb_reviews, lineterminator='\n')
    listing_count = 0
    count = 0
    old_id = ""
    for row in csvReader:
        if(count==0): 
            old_id = row[0]
        data_row = []
        if(old_id != row[0]):
            listing_count +=1
            old_id = row[0]
        if listing_count<50:
            data_row.append(row[0])
            data_row.append(row[1])
            blob = TextBlob(row[2])
            # if(blob.detect_language() == 'en'): 
            #     # blob = blob.translate(from_lang=blob.detect_language(), to='en')
            data_row.append(str(blob.sentiment.polarity))
        else: 
            break
        count+=1
        csv_data.append(data_row)
airbnb_reviews.close()
with open('polarity.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)
csv_file.close()
        # text_reviews.append(blob.sentiment.polarity)
        # date_reviews.append(row[0])


