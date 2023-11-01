#Use Python to calculate the distance (in AU units) between Jupiter and Sun on January 1, 1230.

import ephem

jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
distance_km = jupiter.sun_distance * 149597870.691

print(distance_km)
