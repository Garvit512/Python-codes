import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

texts = ['John likes to watch movies. Mary likes too.',
   'John also likes to watch football games.',
   'Johns mother name is Martha, she likes hockey.',]

vectorizer = CountVectorizer()

BOW = vectorizer.fit_transform(texts)

print(pd.DataFrame(BOW.A, columns=vectorizer.get_feature_names()).to_string())
