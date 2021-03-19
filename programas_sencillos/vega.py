def main ():
    file_name = input("introduce el nombre del fichero: ")
    f = open(file_name, "r")
    text = f.read()

    l = text.find("vega")
    if(l>=0):
        print("si esta")
    else:
        print("no esta")
if __name__ == "__main__":
    main()