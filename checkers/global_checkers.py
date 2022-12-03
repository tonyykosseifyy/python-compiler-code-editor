python_keywords = ["for" , "while" , "if" ,"continue" , "break" ]
python_operators = ["or" , "and" , "\\", "," , "." , "+" , "-" , "/","(",")" ,"=","not","in","&","^","|","~",">","<",":","*","%","=="]

numbers = [0,1,2,3,4,5,6,7,8,9]
def checkNotNumber(f_char):
    for num in numbers :
        if f_char == str(num) :
            return False 
    return True 

def checkVariableExistence(line , global_variables):
    for elmt in line :
        if elmt not in python_operators and elmt not in python_keywords and elmt not in global_variables and elmt[0]!="'" and elmt[0]!='"' and checkNotNumber(elmt[0]):
            return "NameError: name '" + elmt + "' is not defined" 
    

def getIndentation(line):
    indent = 0 
    i = 0 
    while line[i] == "" :
        indent += 1 
        i += 1 

    return indent  

def stripArray(line):
    i = 0
    while line[i] == "" :
        i+=1 
    del line[0:i]
    return line

def stripFromEnd(line):
    print(line)
    if len(line) == 1 :
        return line
    i = len(line) - 1 
    while line[i] == "":
        i-= 1 
    del line[i+1:len(line)]
    return line
