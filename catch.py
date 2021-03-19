# funciones para lectura de ficheros

def gtFile(file_name):
    if (file_name[len(file_name)-3:len(file_name)] == "log"):
        f = open(file_name, "r")
        text = f.read()
        f.close()
        return text 

def gtLine(f):
    text = f.readline()
    return text

def gtLines(f):
    lines = f.readlines()
    return lines
