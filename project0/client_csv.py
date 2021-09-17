from random import randrange
from flask import Flask
import pandas as pd

app = Flask(__name__)


class Questions:
    def __init__(self, location, filename):
        self.loc = location
        self.filen = filename
        file_data = pd.read_csv(filename)  # creates dataframe
        self.questions = file_data

    def get(self, category=1, level=None, qid=None):
        if(qid):  # priority 1, if qid exists, return the column with the qid
            # returns true if qid row corresponds with qid parameter, false otherwise
            filtered_data = self.questions['qid'] == qid
            # returns the row of matching qid
            return self.questions[filtered_data]
        else:
            # returns true if category matches inputed category
            filtered_data = self.questions['category'] == category
            # returns the rows of matching category. dropna drops all na data
            filtered_rows = self.questions[filtered_data].dropna(how='all')
            if (level):
                # returns true if category
                filtered_data = filtered_rows['level'] == level
                filtered_rows = filtered_rows[filtered_data].dropna(
                    how='all')  # returns the rows
            # columns we want to return
            columns_selected = ['qid', 'category', 'level']
            # astype to cast from float to int
            data = filtered_rows[columns_selected]

            return data.sample()  # return a random row from the dataframe


questions = Questions('/', 'questions.csv')

print(questions.questions, '\n\n')

q = questions.get().to_dict(orient='record')[0]
print(q, '\n\n')

q = questions.get(category=2).to_dict(orient='record')[0]
print(q, '\n\n')

q = questions.get(category=1, level=3).to_dict(orient='record')[0]
print(q, '\n\n')

q = questions.get(qid=10).to_dict(orient='record')[0]
print(q, '\n\n')
