class PrintCheck :
    def __init__(self, line , files_variables) :
        self.line = line 
        self.file_variables = files_variables

    def check(self):
        if self.line[1] not in self.file_variables and self.line[1][0] != "'" and self.line[1][0] != '"':
            return "NameError: name '" + self.line[1] + "' is not defined"
    
