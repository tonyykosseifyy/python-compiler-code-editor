from checkers.global_checkers import checkVariableExistence, python_operators
import re 

class Statement:
    def __init__(self , line , file_variables):
        self.line = line
        self.file_variables = file_variables

    def check(self):
            return (
                checkPrint(self.line) or
                checkOperators(self.line , self.file_variables) or 
                checkAfterEqualityOperator(self.line , self.file_variables) or 
                checkMispelledEquality(self.line)
            )


def checkOperators(line , file_variables):
    if line[1] == "==" or line[1] == "!=" or line[1] == ">=" or line[1] == "<=" :
        return checkVariableExistence(line , file_variables)

    if line[1] == "=" :
        return checkVariableExistence(line[2:] , file_variables)
     
def checkAfterEqualityOperator(line, file_variables) :
    if len(line) > 3 :
        for elmt in range(2,len(line)-1,2) :
            if line[elmt] in file_variables :
                if line[elmt + 1] in python_operators :
                    continue
                else :
                    return "SyntaxError: invalid syntax"

def checkMispelledEquality(line):
    if line[1] == ":" :
        return "SyntaxError: invalid syntax"

def checkPrint(line):
    if len(line) == 1:
        return True 
        
