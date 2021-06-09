#!/usr/bin/env python3
import linecheck

def loadDirs(file):
	with open(file) as dirs:
		return [line.rstrip('\n') for line in dirs]

def main():
	linecheck.outputToFile('out', linecheck.lineCheck(loadDirs('dirs.txt')))

if __name__ == '__main__':
	main()