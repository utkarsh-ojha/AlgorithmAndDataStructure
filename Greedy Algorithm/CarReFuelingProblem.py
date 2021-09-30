'''
Problem Definition:
==================
Given a number N which represents the total distance in km to be covered by
a car on a from city A to B. There are N petrol pumps at a distance of some KM.
The capacity of the fuel tank of the car is such that at full tank it goes till a distance of K km.
The car has to compulsorily stop at M gasStations whose distance from the starting position is
given as M integers. The task is to find the number of times, the car has to refill its tank including
the compulsory stops to complete its journey of N km.
'''
# complexity is O(n)

def car_fueling(distFromAToB, mileageOfCar, totalNumOfCitiesBetwnAB, gasStationsDistanceFromA):
    
    noOfTotalRefill, noOfCurrentRefill, carCanReach = 0, 0, mileageOfCar
    
    while carCanReach < distFromAToB:
        # While the destination cannot be reached with current fuel
        if noOfCurrentRefill >= totalNumOfCitiesBetwnAB or gasStationsDistanceFromA[noOfCurrentRefill] > carCanReach:
            # Cannot reach the destination nor the next gas station
            return -1

        # Find the furthest gas station we can reach
        while noOfCurrentRefill < totalNumOfCitiesBetwnAB - 1 and gasStationsDistanceFromA[noOfCurrentRefill + 1] <= carCanReach:
            noOfCurrentRefill += 1

        noOfTotalRefill += 1
        carCanReach = gasStationsDistanceFromA[noOfCurrentRefill] + mileageOfCar
        noOfCurrentRefill += 1
    return noOfTotalRefill


# Getting the distance between the two cities from the user
distFromAToB = int(input("Enter the Distence between City 'A' and City 'B'"))

# Getting the number of possible stops for fueling between City A and City B
totalNumOfCitiesBetwnAB = int(input("Enter the number of cities between A & B"))

# Getting the distance of Gas Stations from the source i.e from 0 (zero) & storing in list
gasStationsDistanceFromA = [int(input("enter distance of {} city from City 'A'".format(city+1))) for city in range(totalNumOfCitiesBetwnAB)]

#Getting the distance the car can go after full tank, from user
mileageOfCar = int(input("Enter the milage of your car when full tank"))

#calling the function car_fueling to get the minimum stop
print(car_fueling(distFromAToB, mileageOfCar, totalNumOfCitiesBetwnAB, gasStationsDistanceFromA))



