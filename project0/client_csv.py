import pandas as pd


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
            # columns we want to return
            # returns the row of matching qid
            data = self.questions[filtered_data]
            if (data.size == 0):
                return {}
            else:
                return data.to_dict(orient='records')[0]
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
            # columns_selected = ['qid', 'category', 'level']
            # astype to cast from float to int
            data = filtered_rows

            if (data.size == 0):
                return {}
            else:
                # return a random row from the dataframe
                return data.sample().to_dict(orient='records')[0]


questions = Questions('/', 'questions.csv')

print(questions.questions, '\n\n')

q = questions.get()
print(q, '\n\n')

q = questions.get(category=2)
print(q, '\n\n')

q = questions.get(category=7, level=3)
print(q, '\n\n')

q = questions.get(qid=10)
print(q, '\n\n')
