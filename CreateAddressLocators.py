#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      allenlee
#
# Created:     20/08/2015
# Copyright:   (c) allenlee 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def createloc():
    #Address Points locator
    arcpy.CreateAddressLocator_geocoding(in_address_locator_style="US Address - Single House",in_reference_data="'//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/NG911_Final.gdb/NG911/AddressPoints' 'Primary Table'",in_field_map="'Feature ID' OBJECTID VISIBLE NONE;'*House Number' HNO VISIBLE NONE;Side <None> VISIBLE NONE;'Prefix Direction' <None> VISIBLE NONE;'Prefix Type' <None> VISIBLE NONE;'*Street Name' RD VISIBLE NONE;'Suffix Type' <None> VISIBLE NONE;'Suffix Direction' <None> VISIBLE NONE;'City or Place' MUNI VISIBLE NONE;'ZIP Code' ZIP VISIBLE NONE;State STATE VISIBLE NONE;Longitude <None> VISIBLE NONE;Latitude LAT VISIBLE NONE;'Street ID' <None> VISIBLE NONE;'Min X value for extent' <None> VISIBLE NONE;'Max X value for extent' <None> VISIBLE NONE;'Min Y value for extent' <None> VISIBLE NONE;'Max Y value for extent' <None> VISIBLE NONE;'Additional Field' <None> VISIBLE NONE;'Altname JoinID' <None> VISIBLE NONE",out_address_locator="//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressPoint_Loc",config_keyword="#")

    #Address Centerline locator
    arcpy.CreateAddressLocator_geocoding(in_address_locator_style="US Address - Dual Ranges",in_reference_data="'//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/NG911_Final.gdb/NG911/RoadCenterline' 'Primary Table';'//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/NG911_Final.gdb/NG911/RoadAlias' 'Alternate Name Table'",in_field_map="'Primary Table:Feature ID' RoadCenterline:OBJECTID VISIBLE NONE;'*Primary Table:From Left' RoadCenterline:L_F_ADD VISIBLE NONE;'*Primary Table:To Left' RoadCenterline:L_T_ADD VISIBLE NONE;'*Primary Table:From Right' RoadCenterline:R_F_ADD VISIBLE NONE;'*Primary Table:To Right' RoadCenterline:R_T_ADD VISIBLE NONE;'Primary Table:Prefix Direction' RoadCenterline:PREFIX VISIBLE NONE;'Primary Table:Prefix Type' <None> VISIBLE NONE;'*Primary Table:Street Name' RoadCenterline:NAME VISIBLE NONE;'Primary Table:Suffix Type' RoadCenterline:TYPE VISIBLE NONE;'Primary Table:Suffix Direction' <None> VISIBLE NONE;'Primary Table:Left City or Place' <None> VISIBLE NONE;'Primary Table:Right City or Place' <None> VISIBLE NONE;'Primary Table:Left ZIP Code' RoadCenterline:ZIP_L VISIBLE NONE;'Primary Table:Right ZIP Code' RoadCenterline:ZIP_R VISIBLE NONE;'Primary Table:Left State' RoadCenterline:STATE_L VISIBLE NONE;'Primary Table:Right State' RoadCenterline:STATE_R VISIBLE NONE;'Primary Table:Left Street ID' <None> VISIBLE NONE;'Primary Table:Right Street ID' <None> VISIBLE NONE;'Primary Table:Min X value for extent' <None> VISIBLE NONE;'Primary Table:Max X value for extent' <None> VISIBLE NONE;'Primary Table:Min Y value for extent' <None> VISIBLE NONE;'Primary Table:Max Y value for extent' <None> VISIBLE NONE;'Primary Table:Left Additional Field' <None> VISIBLE NONE;'Primary Table:Right Additional Field' <None> VISIBLE NONE;'Primary Table:Altname JoinID' RoadCenterline:SEGID VISIBLE NONE",out_address_locator="//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/RoadCenterline_Loc",config_keyword="#")

    #Create Composite Address Locator
    arcpy.CreateCompositeAddressLocator_geocoding(in_address_locators="'//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressPoint_Loc' AddressPoint_L;'//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/RoadCenterline_Loc' RoadCenterline",in_field_map="""Street "Street or Intersection" true true true 100 Text 0 0 ,First,#,//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressPoint_Loc,Street,0,0,//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/RoadCenterline_Loc,Street,0,0;City "City or Placename" true true false 40 Text 0 0 ,First,#,//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressPoint_Loc,City,0,0;State "State" true true false 20 Text 0 0 ,First,#,//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressPoint_Loc,State,0,0,//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/RoadCenterline_Loc,State,0,0;ZIP "ZIP Code" true true false 10 Text 0 0 ,First,#,//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressPoint_Loc,ZIP,0,0,//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/RoadCenterline_Loc,ZIP,0,0""",in_selection_criteria="AddressPoint_L #;RoadCenterline #",out_composite_address_locator="//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressComposite_Loc")


def rebuildloc():

    print "Rebuilding Road Centerline Locator"
    #Rebuild Centerline Locator
    arcpy.RebuildAddressLocator_geocoding(in_address_locator="//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/RoadCenterline_Loc")

    print "Rebuilding AddressPoints Locator"
    #Rebuild Address Points Locator
    arcpy.RebuildAddressLocator_geocoding(in_address_locator="//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressPoint_Loc")

    print "Rebuilding Composite Locator"
    #Rebuild Composite Locator
    arcpy.RebuildAddressLocator_geocoding(in_address_locator="//sncogis/departments/GIS and Mapping/NGen911/NG911__Edit/AddressComposite_Loc")

