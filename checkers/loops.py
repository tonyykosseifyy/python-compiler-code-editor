from checkers.conditions import *

class Loop :
    def __init__(self , line) :
        self.line = line 
    
    def checkFor(self):
        return checkBasic(self.line) 
            

    def checkWhile(self):
        if self.line[0] == "while" :
            return Condition(self.line[1:-1])

    def check(self):
        return self.checkFor() or self.checkWhile()

def checkBasic(line):
    if line[0] == "for":
        if line[2] != "in" or line[3] != "range" :   
            return "SyntaxError: invalid syntax"
        if line[6] != ":":
            return "SyntaxError: invalid syntax"        

        if line[-1] != ":":
            return "SyntaxError: expected ':'"
            
