import re 

class Variable:
    def __init__(self , line, file_variables):
        self.line = line
        self.file_variables = file_variables
        
    def checkErrors(self):
        return (
            startsWithNumber(self.line) or 
            notAllowedVariable(self.line) or 
            startsWithOperator(self.line) or 
            stringVariable(self.line) or 
            checkComma(self.line) or 
            checkCommaAfterEquality(self.line) or 
            checkValuesToUnpack(self.line)
        )

    def giveVariables(self):
        variables_dic = {}
        if "," not in self.line[0] :
            variables_dic[self.line[0]] = self.line[2]

        else :
            variables_list = self.line[0].split(",")
            values_list = self.line[2].split(",")
            for i in range(len(variables_list)):
                variables_dic[variables_list[i]] = values_list[i] 

        return variables_dic




def startsWithNumber(line):
    for i in range(10):
        if line[0][0] == str(i):
            return "SyntaxError: invalid decimal literal"

def notAllowedVariable(line):
    if  "-" in line[0] or  "/" in line[0] or "\\" in line[0]:
            return "SyntaxError: invalid syntax"


def startsWithOperator(line):

    if line[0] == "=" or line[0] == "-" or line[0] == "+" or line[0] == "/" :
        return "SyntaxError: cannot assign to expression here"


def stringVariable(line):
    f_char = line[0][0]
    l_char = line[0][-1]
    if f_char == "'" or f_char == '"' or l_char=="'" or l_char=='"' :
        return "SyntaxError: cannot assign to literal here."


def checkComma(line):
    if "," in line[0] :
        list = line[0].split(",")
        if list[0] == "":
            return "SyntaxError: invalid syntax"
        if list[1] == "":
            return "TypeError: cannot unpack non-iterable int object"

        ## Add 2 variables 

def checkCommaAfterEquality(line):
    if "," in line[2] :
        list = line[2].split(",")
        if list[0] == "":
            return "SyntaxError: invalid syntax"


def checkValuesToUnpack(line):
    if "," in line[2] and "," in line[0] :
        variable_list = line[0].split(",")
        values_list = line[2].split(",")

        if len(variable_list) > len(values_list):
            return "ValueError: too many values to unpack (expected " +  str(len(variable_list)) + ")"  
    
        if len(values_list) > len(variable_list) :
            return "ValueError: too many values to unpack (expected " +  str(len(variable_list)) + " got " + str(len(values_list)) + ")"

