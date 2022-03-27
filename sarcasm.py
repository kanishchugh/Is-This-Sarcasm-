import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

class Sarcasm:
    def __init__(self, path):
        self.df = pd.read_json(path, lines=True)

    def preprocessing(self):
        self.df["is_sarcastic"] = self.df["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
        self.df = self.df[["headline", "is_sarcastic"]]
        X = np.array(self.df["headline"])
        self.y = np.array(self.df["is_sarcastic"])
        self.cv = CountVectorizer()
        self.X = self.cv.fit_transform(X)
    
    def split(self):
        self.preprocessing()    
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
    
    def model(self):
        self.split()
        self.model = BernoulliNB()
        self.model.fit(self.X_train,self.y_train)
    
    def run(self):
        self.model()
        user = input("Enter a text: ")
        data = self.cv.transform([user]).toarray()
        output = self.model.predict(data)
        print(output[0])
sarcasm = Sarcasm(path='./data/Sarcasm.json')
sarcasm.run()
