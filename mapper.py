#!/usr/bin/python

import sys
import StringIO

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        # This is the place you need to do some defensive programming
        # what if there are not exactly 6 fields in that line?
      
        if len(data) == 6:

        # this next line is called 'multiple assignment' in Python
        # this is not really necessary, we could access the data
        # with data[2] and data[5], but we do this for conveniency
        # and to make the code easier to read
         date, time, store, item, cost, payment = data

        # Now print out the data that will be passed to the reducer
        print "{0}\t{1}".format(item, cost)


# This function allows you to test the mapper with the provided test string
def main():
	# sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
