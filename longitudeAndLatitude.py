import math

def main():
    lat1=eval(input("Enter Latitude for Point 1: "))
    lon1=eval(input("Enter Longitude for Point 1: "))
    lat2= eval(input("Enter Latitude for Point 2: "))
    lon2= eval(input("Enter Longitude for Point 2: "))

    distance=getDistanceInMiles(lat1,lon1,lat2,lon2)
    print("Distance apart in miles:",distance)

def getDistanceInMiles(lat1,lon1,lat2,lon2):
    milesConv=0.62137119224
    
    earthRadius = 6371; ##Radius of earth in kilometers
    distanceLat = deg2rad(lat2-lat1)  
    distanceLon = deg2rad(lon2-lon1);
    a = math.sin(distanceLat/2) * math.sin(distanceLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(distanceLon/2) * math.sin(distanceLon/2)
    formula = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
    distance = earthRadius * formula*milesConv
    return distance


def deg2rad(deg):
    return deg * (math.pi/180)




if __name__=='__main__':
    main()

