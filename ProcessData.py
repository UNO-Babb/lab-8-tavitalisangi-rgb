#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    if not line.strip():
      continue 
    data = line.split()
    first = data[0]
    last = data [1]
    idnum = data[3]
    dob = data[4]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idnum)
    majoryear = makeMajoryear(major, year)
    output = last + "," + first + "," + student_id + "," + majoryear + "\n"
    outFile.write(output)
    #print(student_id)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idnum):
  #print(first,last, idnum)
  idlen = len(idnum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idnum[idlen - 3: ].lower()

  #print(id)
  return id

def makeMajoryear(major, year):
  code = major[:3].title()

  year_map = {"Freshman": "FR", "Sophomore": "SO", "Junior": "JR", "Senior": "SR"}
  year2 = year_map.get(year, year[:2].upper())
  return code + "-" + year2

if __name__ == '__main__':
    main()
