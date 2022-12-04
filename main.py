from checkers.variables import *
from checkers.conditions import *
from checkers.statements import * 
from checkers.print import *
from checkers.loops import *
from checkers.global_checkers import getIndentation, stripArray,stripFromEnd

def readFromFile(file_name):
    file = open(file_name , "r")
    line_list = []
    for line in file :
        line_list.append(line.split("\n")[0])
    return line_list

##lines = readFromFile("./text.txt")
file_variables = {}
indentation = {"indent": 0 , "required": False , "block": "none"}

def assignVaribales(varibles_dic):
    for key in varibles_dic :
        file_variables[key] = varibles_dic[key]
    

class Line :
    line_count = 1
    def __init__(self, line):
        self.line = stripFromEnd(line.split(" "))
        self.line_count = Line.line_count
        Line.line_count+=1
    
    def checkIndent(self):
        print("indent: ",self.line)
        line_ind = getIndentation(self.line)
        if line_ind > 0 and indentation["indent"] == 0 :
            return "IndentationError: unexpected indent"
        if line_ind < ( 4 * indentation["indent"]) and indentation["required"] :
            return "IndentationError: expected an indented block after '" + str(indentation["block"])+ "' statement on line " + str(self.line_count)

        if line_ind >= (4 * indentation["indent"]) and indentation["required"] :
            indentation["required"] = False 

        elif line_ind <= ( 4 * indentation["indent"]) and not indentation["required"] and line_ind % 4 == 0 :
            indentation["indent"] = line_ind
        
        elif  line_ind <= ( 4 * indentation["indent"]) and not indentation["required"] and line_ind % 4 != 0:
            return "IndentationError: unindent does not match any outer indentation level"
        
        self.line = stripArray(self.line)


    def check(self):
        return self.checkIndent() or self.checkVariable() or self.checkConditions() or self.checkStatement() or self.printCheck() or self.loopCheck()
    
    def checkConditions(self):
        if self.line[0] == "if" or self.line[0] == "elif" or self.line[0] == "else" :
            indentation["indent"]+=1
            indentation["required"] = True 
            indentation["block"] = self.line[0]
            cond = Condition(self.line , file_variables)
            return cond.check()

    def checkVariable(self):
        if len(self.line) == 3 and "=" in self.line and "!=" not in self.line and ">=" not in self.line and "<=" not in self.line and "==" not in self.line:
            variable_line = Variable(self.line, file_variables)
            errors = variable_line.checkErrors() 
            if errors :
                return errors
            assignVaribales(variable_line.giveVariables())

        else :
            return self.checkStatement()
    
    def loopCheck(self):
        if self.line[0] == "for" or self.line[0] == "while":
            indentation["indent"]+=1
            indentation["required"] = True 
            indentation["block"] = self.line[0]
            loop = Loop(self.line)
            errors = loop.check()
            if errors :
                return errors 
            assignVaribales(loop.giveVariable())

    def printCheck(self):
        if self.line[0] == "print" or self.line[0] == "print(":
            p = PrintCheck(self.line, file_variables)
            return p.check()

    def checkStatement(self):
        if self.line[0] != "if" and self.line[0] != "elif" and self.line[0] != "else":
            statement = Statement(self.line , file_variables)
            return statement.check()
        return None 
"""
for line in range(len(lines)) :
    print(line+1,Line(lines[line]).check())
"""


print(file_variables)