def convertTabToIndent(line):
    if "\t" in line :
        tabs = line.count("\t")
        line_list = []
        for i in line :
            if i != "\t" :
                line_list.append(i)
        
        for _i in range(tabs*4):
            line_list.insert(0 , "")
        
        str = ""
        for i in range(tabs*4):
            str+=" "
        for i in range(tabs*4, len(line_list)):
            str+=line_list[i]
        return str 

    return line 


print(convertTabToIndent("print(i)"))

