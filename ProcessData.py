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



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
