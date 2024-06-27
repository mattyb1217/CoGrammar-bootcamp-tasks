import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
model= spacy.load('en_core_web_sm')
model.add_pipe('spacytextblob')

df=pd.read_csv('amazon product reviews.csv')
# print(df.head())

# df.isnull().sum()

# cleaned_data= df.dropna(subset=['reviews.text'])
# cleaned_data

# reviewed_data= df['reviews.text']
# reviewed_data

def clean_text(text):
    text= str(text).lower().strip()

#process with spaCy
    doc=model(text)

    cleaned_tokens= [token.text for token in doc if token.is_stop and token.is_alpha]
    cleaned_text= ' '.join(cleaned_tokens)

    return cleaned_text

df['cleaned_reviews']= df['reviews.text'].apply(clean_text)
df.head()

#polarity
doc= model(df['cleaned_reviews'][4])
polarity= doc._.blob.polarity

def analyse_sentiment(text):
    doc=model(text)

    polarity= doc._.blob.polarity

    if polarity>0:
        sentiment = 'Positive'
    elif polarity<0:
        sentiment='Negative'
    else:
        sentiment='Neutral'

    return sentiment

# comparing sentences
first_comment= df['cleaned_reviews'][34]
second_comment= df['cleaned_reviews'][11]

print(first_comment)
print(second_comment)

print(analyse_sentiment(first_comment))
print(analyse_sentiment((second_comment)))