#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      allenlee
#
# Created:     18/08/2015
# Copyright:   (c) allenlee 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# takes the "L_F_ADD","L_T_ADD","R_F_ADD","R_T_ADD" fields and adds them to a field name MAP_RANGE
# MAP_RANGE is used for labeling centerlines to easily see ranges of all segments
import arcpy

fc = r'\\sncogis\Departments\GIS and Mapping\NGen911\Shawnee_KSNG911N_subFinal\Shawnee_KSNG911N.gdb\NG911\RoadCenterline'

# Start an edit session. Must provide the worksapce.
edit = arcpy.da.Editor(r'\\sncogis\Departments\GIS and Mapping\NGen911\Shawnee_KSNG911N_subFinal\Shawnee_KSNG911N.gdb')

# Edit session is started without an undo/redo stack for versioned data
#  (for second argument, use False for unversioned data)
edit.startEditing(False, False)

# Start an edit operation
edit.startOperation()


fields = ["L_F_ADD","L_T_ADD","R_F_ADD","R_T_ADD","MAP_RANGE"]

count = 0
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        count = count + 1
        lst = []
        L_T_ADD = row[1]
        R_T_ADD = row[3]
        R_F_ADD = row[2]
        L_F_ADD = row[0]
        lst.append(L_T_ADD)
        lst.append(R_T_ADD)
        lst.append(R_F_ADD)
        lst.append(L_F_ADD)
        row[4] = str(min(lst)) + ' - ' + str(max(lst))
        cursor.updateRow(row)
        print "Row",count,"Updated" #count the rows as they are updated

# Stop the edit operation.
edit.stopOperation()

# Stop the edit session and save the changes
edit.stopEditing(True)
