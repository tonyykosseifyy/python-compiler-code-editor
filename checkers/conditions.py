from checkers.global_checkers import *



class Condition :
    def __init__(self, line, file_variables):
        self.line = line 
        self.file_variables = file_variables

    def check(self):
        return ( 
            checkEnd(self.line) or 
            checkEqualityCondition(self.line) or 
            checkVariableExistence(self.line, self.file_variables)
        )
    


def checkEnd(line) :
    if line[-1] != ":" :
        return "SyntaxError: expected ':'" 

def checkEqualityCondition(line):
    if "=" in line :
        if "==" not in line and "!=" not in line and ">=" not in line and "<=" not in line :
            return "SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?" 
 