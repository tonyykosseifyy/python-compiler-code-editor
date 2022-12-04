class PrintCheck :
    def __init__(self, line , files_variables) :
        self.line = line 
        self.file_variables = files_variables

    def check(self):
        if self.line[0] == "print" :
            index = 2
        elif self.line[0] == "print(" :
            index = 1

        if self.line[index] not in self.file_variables and self.line[index][0] != "'" and self.line[index][0] != '"':
            return "NameError: name '" + self.line[index] + "' is not defined"
    

