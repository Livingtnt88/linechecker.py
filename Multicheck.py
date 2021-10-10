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

import linecheck

def loadDirs(file):
	with open(file) as dirs:
		return [line.rstrip('\n') for line in dirs]

def main():
	linecheck.outputToFile('out', linecheck.lineCheck(loadDirs('dirs.txt')))

if __name__ == '__main__':
	main()
