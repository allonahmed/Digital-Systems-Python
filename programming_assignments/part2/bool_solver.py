import sys
sys.path.append("../part0")
from client_csv import *

class BoolEvalSimple:

    def __init__ (self):
        self.row = None

    def set_row(self, row):
        self.row = row

    def bool_eval(self):
        description = self.row["description"] #get description value from dictionary
        problem = self.row["problem"] #get problem value from dictionary
        for variable in description.split(","): #loop through string seperated by comma by using split function
            globals()[str(variable[0])] = int(variable[2]) #creating variables using globals(), our substring[0] will represent the name of the variable and substring[2] represents the value
        return str(int(eval(problem))) #evaluate the expression using eval (note: we cast it to an int to get binary representation of True/False, then cast it as a string as that is our required return value)
        
