# -*- coding: utf-8 -*-
"""
Created on Mon May 08 08:50:05 2017

@author: tih
"""
def Add_Inlets(Name_NC_Runoff, Inflow_Text_Files):
    '''
    This functions add inflow to the runoff dataset before the channel routing.
    The inflow must be a text file with a certain format. The first line of this format are the latitude and longitude.
    Hereafter for each line the time (ordinal time) and the inflow (m3/month) seperated with one space is defined. See example below:
        
    [lat lon]
    733042 156225.12
    733073 32511321.2
    733102 212315.25
    733133 2313266.554
    ''' 
    # General modules
    import numpy as np

    # Water Accounting modules
    import wa.General.raster_conversions as RC
    import wa.Functions.Start.Area_converter as Area

    # Open information and open the Runoff array
    Runoff_dataCube = RC.Open_nc_array(Name_NC_Runoff)
    geo_out, epsg, size_X, size_Y, size_Z, Time = RC.Open_nc_info(Name_NC_Runoff)

    # Calculate the surface area of every pixel
    dlat, dlon = Area.Calc_dlat_dlon(geo_out, size_X, size_Y)
    area_in_m2 =  dlat * dlon
        
    for Inflow_Text_File in Inflow_Text_Files:

        # Open the inlet text data
        Inlet = np.genfromtxt(Inflow_Text_File, dtype=None, delimiter=" ")

        # Read out the coordinates
        Coord = Inlet[0,:]
        Lon_coord = Coord[0][1:]
        Lat_coord = Coord[1][:-1]

        # Search for the pixel
        lon_pix = int(np.ceil((float(Lon_coord) - geo_out[0])/geo_out[1]))
        lat_pix = int(np.ceil((float(Lat_coord) - geo_out[3])/geo_out[5]))

        # Add the value on top of the Runoff array
        for i in range(1, len(Inlet)):
            time = float(Inlet[i,0])
            time_step = np.argwhere(np.logical_and(Time>=time,Time<=time))
            if len(time_step) > 0:
                time_step_array = int(time_step[0][0])
                value_m3_month = float(Inlet[i,1])
                area_in_m2_pixel = area_in_m2[lat_pix, lon_pix]
                value_mm = (value_m3_month/area_in_m2_pixel) * 1000		
                Runoff_dataCube[time_step_array,lat_pix, lon_pix] = Runoff_dataCube[time_step_array,lat_pix, lon_pix] + value_mm
             
    return(Runoff_dataCube)