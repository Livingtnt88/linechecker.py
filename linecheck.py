#!/usr/bin/env python3

import sys, getopt

def lineCheck(FileToCheck, count = 70):
    if type(FileToCheck) == list:
        out = ""
        for file in FileToCheck:
            out = "{Out}\n{File}:\n{content}".format(Out = out, File = file, content = lineCheck(file, count))
        return out
    try:
        FileToCheck = str(FileToCheck.strip("'"))
        FileToCheck = FileToCheck.strip('"')
        reader = open(FileToCheck)
        lines = list(reader)
        reader.close()

    except FileNotFoundError:
        return "Error: file not found"

    out = ""
    for i in range(len(lines)):
        if len(lines[i]) >= count:
            out = out + "\n" + str(i + 1) + " " + str(len(lines[i])) + ' ' + lines[i]
    return out

def outputToFile(fileName, data):
    fileName = str(fileName)
    if not (fileName[-4:] == ".txt"):
        fileName = fileName + ".txt"

    try:
        file = open(fileName, "x")
        file.write(data)
        file.close()
        print("write to", fileName, "successful!")

    except FileExistsError:
        print("Error: a file with the name", fileName, "already Exists")
        Errortext = "would you like to overwrite(O) " + fileName + ", or create a new file(N) " + fileName[:-4] + "NEW.txt? "
        choice = input(Errortext)

        if choice == "O":
            if input("please type 'OVERWRITE' to confirm selection ") == "OVERWRITE":
                print("confirmed overwriting", fileName)
                file = open(fileName, "w")
                file.write(data)
                file.close()
                print("write to", fileName, "successful!")
            else:
                print("unable to confirm input exiting")
                sys.exit(-3)
        
        elif choice == "N":
            outputToFile(fileName[:-4] + "NEW.txt", data)
        
        else:
            print("unable to confirm input exiting")
            sys.exit(-3)

def main(argv):
    noInputMsg = 'Please enter the path of the file to check '
    if argv == []:
        inputFile = input(noInputMsg)
        inputFile = list(map(str.strip, inputFile.strip('][').replace('"', '').split(',')))
        print(lineCheck(inputFile))
        input("Press enter to exit")
        sys.exit(0)
    
    inputFile = ""
    outputFile = ""
    output = ""
    count = 70

    i = False
    o = False

    try:
        opts, args = getopt.getopt(argv, "hi:o:c:")
    except getopt.GetoptError:
        print(sys.argv[0], "-i <inputfile> -o <outputfile> -c <chacter count>")
        sys.exit(-1)
    
    for opt, arg in opts:
        if opt == "-h":
            print(sys.argv[0], "-i <inputfile> -o <outputfile> -c <character count>")
            sys.exit(0)
        elif opt == "-i":
            inputFile = arg
            i = True
        elif opt == "-o":
            outputFile = arg
            o = True
        elif opt == "-c":
            try:
                count = int(arg)
                if count <= 0:
                    raise ValueError
            except (TypeError, ValueError):
                print("Error: Character count argument must be a positve interger")
                sys.exit(-2)
    
    if i:
        if inputFile[0] == '[':
            inputFile = list(map(str.strip, inputFile.strip('][').replace('"', '').split(',')))
            for file in inputFile:
                print(file)
        output = lineCheck(inputFile, count)
    else:
        output = lineCheck(input(noInputMsg), count)

    if o:
        outputToFile(outputFile, output)
    else:
        print(output)

if __name__ == "__main__":
    main(sys.argv[1:])