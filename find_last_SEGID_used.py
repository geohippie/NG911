#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lee Allen
#
# Created:     /2015
# Updated 4/11/2016 to report/accept non number values if they occur in data field
# Copyright:   (c) Lee Allen 2015
# License:     Use at your convenience
#-------------------------------------------------------------------------------

#find the first and last SEGID or ADDID. Make sure GenerateID value is higher than last SEGID or ADDID
#skips rows that are not numbers

streetcursor = arcpy.da.SearchCursor("RoadCenterline","SEGID")
seglist = []
for row in streetcursor:
    SEGID = row[0]
    try:
        SEGID = int(row[0])
        seglist.append(SEGID)
    except:
        print 'Segment ID ', SEGID,' is not a number'
        pass

seglist.sort()
print "First SEGID =", seglist[0],"Last SEGID =",seglist[-1]

apointcursor = arcpy.da.SearchCursor("AddressPoints","ADDID")
pointlist = []
for row in apointcursor:
    try:
        ADDID = int(row[0])
        pointlist.append(ADDID)
    except:
        print 'Point ID ' , ADDID ,' is not a number'
        pass

pointlist.sort()
print "First ADD =", pointlist[0],"Last ADDID =",pointlist[-1]

##testlist = [1,5,8,12,55,0,3,7,66,'aaa',999,21,75]
##segtestlist = []
##for num in testlist:
##    SEGID = num
##    try:
##        if SEGID/1:
##            SEGID = int(num)
##            segtestlist.append(SEGID)
##    except:
##        print 'ID ' + SEGID +' is not a number'
##        pass
##
##segtestlist.sort()
##print "First SEGID =", segtestlist[0],"Last SEGID =",segtestlist[-1]
### should print: ID aaa is not a number  First SEGID = 1 Last SEGID = 999
