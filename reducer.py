#!/usr/bin/python
import sys
#initials 
salesTotal = 0
oldKey = None


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone bad. Skip this line.
        continue

    thisKey, thisSale = data
    if oldKey != thisKey:
          if oldKey is not None:
		print "{0}\t{1}".format(oldKey, salesTotal)
	  oldKey=thisKey
	  salesTotal =0

#calculate 
    salesTotal+=float(thisSale)
#print the output
if oldKey != None:
    print oldKey, "," salesTotal
