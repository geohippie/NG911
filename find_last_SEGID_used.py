#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lee Allen
#
# Created:     /2015
# Copyright:   (c) Lee Allen 2015
# Licence:     Use at your convenience
#-------------------------------------------------------------------------------

#find the first and last SEGID or ADDID. Make sure GenerateID value is higher than last SEGID

streetcursor = arcpy.da.SearchCursor("RoadCenterline","SEGID")
seglist = []
for row in streetcursor:
    SEGID = int(row[0])
    seglist.append(SEGID)

seglist.sort()
print "First SEGID =", seglist[0],"Last SEGID =",seglist[-1]

apointcursor = arcpy.da.SearchCursor("AddressPoints","ADDID")
pointlist = []
for row in apointcursor:
    ADDID = int(row[0])
    pointlist.append(ADDID)

pointlist.sort()
print "First ADD =", pointlist[0],"Last ADDID =",pointlist[-1]


##testlist = [1,5,8,12,55,0,3,7,66,999,21,75]
##segtestlist = []
##for num in testlist:
##    SEGID = num
##    segtestlist.append(SEGID)
##
##segtestlist.sort()
##print "First SEGID =", segtestlist[0],"Last SEGID =",segtestlist[-1]
### should print: First SEGID = 0 Last SEGID = 999
