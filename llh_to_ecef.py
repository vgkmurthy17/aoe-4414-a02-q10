# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_degrees long_degrees hae_km
# Converts LLH to ECEF
# 
# Parameters:
#  lat_degrees: Latitude (deg)
#  long_degrees: Longitude (deg)
#  hae_km: Height above ellipsoid (km)
# Output:
#  Prints the ECEF x, y, z coordinates in km
#
# Written by Vineet Keshavamurthy
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

import math
import sys

# Constants
R_E_KM = 6378.1363   # Earth's radius (km)
E_E = 0.081819221456  # Earth's eccentricity

# Helper function to calculate denominator
def calc_denom(ecc, lat_radian):
    return math.sqrt(1.0 - (ecc ** 2) * (math.sin(lat_radian) ** 2))

# Parse script arguments
if len(sys.argv) != 4:
    print("Usage: python3 llh_to_ecef.py lat_degrees long_degrees hae_km")
    exit()

lat_degrees = float(sys.argv[1])
long_degrees = float(sys.argv[2])
hae_km = float(sys.argv[3])

# conver the given variables into radians
lat_radian = math.radians(lat_degrees)
long_radian = math.radians(long_degrees)

# C_E and S_E Calculation
C_E = R_E_KM / (calc_denom(E_E, lat_radian))
S_E = (R_E_KM*(1-E_E**2)) / calc_denom(E_E, lat_radian)

# Calculate ECEF coordinates after finding C_E and S_E
r_x = (C_E + hae_km) * math.cos(lat_radian) * math.cos(long_radian) #r_x component

r_y = (C_E + hae_km) * math.cos(lat_radian) * math.sin(long_radian) #r_y component

r_z = (S_E + hae_km) * math.sin(lat_radian) #r_z component

# Print the ECEF coordinates rounded to 6 decimal places
print(round(r_x, 6)) #r_x

print(round(r_y, 6)) #r_y

print(round(r_z, 6)) #r_z
