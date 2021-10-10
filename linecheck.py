#!/usr/bin/env python3

#    Copyright (C) 2021 LivingTNT88
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys, getopt

def lineCheck(FileToCheck, count = 70):
    out = "linenumber Charactercount line"
    if type(FileToCheck) == list:
        for file in FileToCheck:
            out += f"\n{file}:\n{lineCheck(file, count)}"
        return out
    try:
        FileToCheck = str(FileToCheck.strip("'"))
        FileToCheck = FileToCheck.strip('"')
        reader = open(FileToCheck)
        lines = list(reader)
        reader.close()

    except FileNotFoundError:
        return "Error: file not found"

    for i in range(len(lines)):
        if len(lines[i]) >= count:
            out += f"\n{i + 1} {len(lines[i])} {lines[i]}"
    return out

def outputToFile(fileName, data):
    fileName = str(fileName)
    if not (fileName[-4:] == ".txt"):
        fileName += ".txt"

    try:
        file = open(fileName, "x")
        file.write(data)
        file.close()
        print("write to", fileName, "successful!")

    except FileExistsError:
        print("Error: a file with the name", fileName, "already Exists")
        choice = input(f"would you like to overwrite(O) {fileName}, or create a new file(N) {fileName[:-4]}NEW.txt? ")

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
