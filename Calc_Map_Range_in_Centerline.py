#-------------------------------------------------------------------------------
# Name:        Calculate Field Map Range or Label expression with Map Range
# Purpose:      Calculate Field Map Range or Label expression with Map Range
#
# Author:      Lee Allen
#
# Created:     04/11/2016
# Copyright:   (c) Lee Allen 2016
# License:     Use at your earliest convenience
#-------------------------------------------------------------------------------
#For just labeling---->Below

#While in Editing Session - Right Click MAP RANGE field in table>Field Calculator
#Enter data as shown below

#select Python
#check Show Codeblock

# Pre-Logic Script Code:
def map_range(L_T_ADD,R_T_ADD,R_F_ADD,L_F_ADD):
    lst = []
    lst.append(L_T_ADD)
    lst.append(R_T_ADD)
    lst.append(R_F_ADD)
    lst.append(L_F_ADD)
    mrange = str(min(lst)) + ' - ' + str(max(lst))
    return mrange

#MAP_RANGE =
map_range( !L_T_ADD!, !R_T_ADD!, !R_F_ADD!, !L_F_ADD!)

##---------------LABEL ADDRESS RANGES-----------------------------
##  USE INSTEAD of Calculating field
##  Check Display coded value description
##  Check Advanced
##  Parser is Python

def FindLabel ( [L_T_ADD] , [R_T_ADD] , [R_F_ADD] , [L_F_ADD] ):
    lst = []
    lst.append([L_T_ADD])
    lst.append([R_T_ADD])
    lst.append([R_F_ADD])
    lst.append([L_F_ADD])
    mrange = str(min(lst)) + ' - ' + str(max(lst))
    return mrange

##---------------LABEL ADDRESS RANGES and Road NAME using LABEL Field -----------------------------
##  USE INSTEAD of Calculating field
##  Check Display coded value description
##  Check Advanced
##  Parser is Python

## Returns the Street LABEL as well as a Map Range

def FindLabel ([L_T_ADD] ,[R_T_ADD] ,[R_F_ADD] ,[L_F_ADD], [LABEL]):
    lst = []
    lst.append([L_T_ADD])
    lst.append([R_T_ADD])
    lst.append([R_F_ADD])
    lst.append([L_F_ADD])
    mrange = str(min(lst)) + ' - ' + str(max(lst))
    label = [LABEL] 
    namerange = label + '  ' + str(mrange)
    return namerange
