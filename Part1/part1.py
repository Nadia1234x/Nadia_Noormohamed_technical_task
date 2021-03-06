#Name: Nadia Noormohamed

import requests
import time
from operator import itemgetter
import multiprocessing


filterByNoPassengers = 0

#Options
print "\nTo use test data for pickup and dropoff latitudes and longitudes" ,\
"please enter 1"

print "\nTo enter the data manually please enter 2"
latAndLongOption = filterByNoPassengers = int(raw_input("Please enter the option number:"))

#Test data
if(latAndLongOption == 1):
    latitudePickup = "3.410632"
    longitudePickup = "-2.157533"
    latitudeDropoff = "3.410632"
    longitudeDropoff = "-2.157533"
else:
    print "adding"
    latitudePickup = raw_input("please enter the pickup latitude: ")
    longitudePickup = raw_input("please enter the pickup longitude: ")
    latitudeDropoff = raw_input("please enter the dropoff latitude: ")
    longitudeDropoff = raw_input("please enter the dropoff longitude: ")

print "Do you want to filter the taxis available based on the number of", \
"passsengers?"
print "Enter 1 for Yes"
print "Enter 2 for No"
filterByNoPassengers = int(raw_input("Please enter the option number:"))

if(filterByNoPassengers == 1):
        numberOfPassengers = int(raw_input
        ("Please enter the number of passenger travelling: "))

print "Would you like to search all suppliers for a taxi, or a specific one?"
print "Enter 1 to search all suppliers"
print "Enter 2 to search for a taxi from a specific supplier"
allOrOne = int(raw_input("Please enter the option number:"))


supplier1 = "Dave"
supplier2 = "Eric"
supplier3 = "Jeff"
requestBooking = 0



def makeBookingRequest(supplierName):
    # 1) making the request
    #output depends on the number of passengers - console application to print
    #the search results for Dave's taxi's
    url = "https://techtest.rideways.com/"
    #timeResponse(supplierName)
    requestBooking = executeBookingRequest(url, supplierName)



    if(requestBooking.status_code == 400):
        print "You are not making the request correctly, please check the URL",\
        "and parameters"

    #if response to request failed - handles by making request until successful
    if(requestBooking.status_code == 500):
            requestBooking = executeBookingRequest(url, supplierName)
    respToReq = requestBooking.text
    #response to request successful
    if(requestBooking.status_code == 200):
            #if(allOrOne == 2):
            print "\nResults for", supplierName, "Taxis:"
            try:
                print "Please use to check the final output\n", respToReq
                partition1 = respToReq.split('":[')
                part2 = partition1[1]
                unused, partition2 = part2.split('{', 1)
                partition2, unused = partition2.rsplit('}]}', 1)
                partition2 = partition2.split('},{')
                partition2 = list(partition2)
                partition2 = [str(r) for r in partition2]
                carTypeList = [i.split(',')[0] for i in partition2]
                pricesList = [int(i.split('"price":')[-1]) for i in partition2]

                #sorting the car types in descending order of their price.
                sortedCombinedList = sortDescendingOrder(carTypeList,
                pricesList)

                #Changing the tuple back to 2 separate lists.
                carTypeList, pricesList = zip(*sortedCombinedList)

                #print all the car types available by a supplier if number of
                #passengers travelling not specified.

                if(filterByNoPassengers == 2):
                    if(allOrOne == 2):
                        for x in range(len(carTypeList)):
                            print  carTypeList[x], ",price:", pricesList[x]
                    else:
                        return zip(carTypeList, pricesList)

                #otherwise print the filtered car types based on the no. of
                #passengers
                else:
                    combinedFilteredList = filterSearchResultsForOneSupplier(sortedCombinedList, list(carTypeList), list(carTypeList), list(pricesList),list(pricesList))
                    return combinedFilteredList
                    #return combinedFilteredList

            # if no cars available by the supplier then catch the exception
            # caused by the split function.
            except ValueError:
                print "Sorry, There are no cars available by supplier:",\
                supplierName, "at the moment, please try again later."


def filterSearchResultsForOneSupplier(combinedList, carType, carTypeOld,pricesList, pricesListOld):
    loopAround = 1
    filCarTypeList = []
    filPricesList = []


    while(loopAround <= 6):


            if(numberOfPassengers <= 4):
                if(loopAround == 1):
                    substring = '"STANDARD"'
                    removeElementfromList(substring, carType, pricesList)

            if(numberOfPassengers <= 4):
                if(loopAround == 2):
                    substring = '"EXECUTIVE"'
                    removeElementfromList(substring, carType, pricesList)

            if(numberOfPassengers <= 4):
                if(loopAround == 3):
                    substring = '"LUXURY"'
                    removeElementfromList(substring, carType, pricesList)

            if(numberOfPassengers <= 4 or (numberOfPassengers > 4
            and numberOfPassengers <= 6)):
                if(loopAround == 4):
                    substring = '"PEOPLE_CARRIER"'
                    removeElementfromList(substring, carType, pricesList)

            if(numberOfPassengers <= 4 or (numberOfPassengers > 4
            and numberOfPassengers <= 6)):
                if(loopAround == 5):
                    substring = '"LUXURY_PEOPLE_CARRIER"'
                    removeElementfromList(substring, carType, pricesList)

            if(loopAround == 6):
                substring = '"MINIBUS"'
                removeElementfromList(substring, carType, pricesList)

            loopAround = loopAround + 1

    #form a list that is the difference between the old list and the list
    #containing the car types not compatible for the number of passenger to
    # give a list of car types compatible for the number of passengers.
    s1 = set(carType)
    carType = [x for x in carTypeOld if x not in s1]

    s2 = set(pricesList)
    pricesList = [x for x in pricesListOld if x not in s2]


    #list = sortDescendingOrder(filCarTypeList, filPricesList)
    #carType = list(set(carTypeOld) - set(carType))
    if(allOrOne == 2):
        print "\nSearch Results:"
        for x in range(len(carType)):
            print carType[x], "price: ", pricesList[x]

    combinedFilteredList = list(zip(carType, pricesList))
    return combinedFilteredList

def executeBookingRequest(URL, supplierName):
    requestBooking = requests.get(URL + supplierName +"?pickup=" +latitudePickup
        + "," + longitudePickup + "&dropoff=" + latitudeDropoff + ","
        + longitudeDropoff)
    return requestBooking

def removeElementfromList(substring, listIn, listIn2):
    returnedValue = next((s for s in listIn if substring in s), None)
    if(returnedValue != None):
        index = listIn.index(returnedValue)
        listIn.remove(returnedValue)
        listIn2.remove(listIn2[index])
        return listIn

def return_index(substring, listIn):
    returnedValue = next((s for s in listIn if substring in s), None)
    if(returnedValue != None):
        index = listIn.index(returnedValue)
        return index


def sortDescendingOrder(carType, prices):
    combinedList = zip(carType, prices)
    sortedCombinedList =  sorted(combinedList, key=itemgetter(1), reverse = True)
    return sortedCombinedList

def sortDescendingOrder2(carType, prices, supplier):
    combinedList = zip(carType, prices, supplier)
    sortedCombinedList =  sorted(combinedList, key=itemgetter(1), reverse = True)
    return sortedCombinedList

def timeResponse(supplierName):
    process = multiprocessing.Process(target=executeBookingRequest,
    name="executeBookingRequest", args=("https://techtest.rideways.com/"
    , supplierName))
    process.start()
    # Wait 2 seconds
    time.sleep(2)
    # Terminate function
    process.terminate()
    process.join()


def filterResultsForAllSuppliers(DavesList, EricsList, JeffsList):

    price1 = None
    price2 = None
    price3 = None
    price_index1 = None
    price_index2 = None
    price_index3 = None
    cheapestCarTypes = []
    pricesList = []
    supplier = []

    numberOfActiveSuppliers = 0
    if(DavesList != None):
        numberOfActiveSuppliers = numberOfActiveSuppliers + 1
    if(EricsList != None):
        numberOfActiveSuppliers = numberOfActiveSuppliers + 1
    if(JeffsList != None):
        numberOfActiveSuppliers = numberOfActiveSuppliers + 1

    if(numberOfActiveSuppliers == 1):
        if(DavesList != None):
            DavesCarTypeList, DavesPricesList = zip(*DavesList)
            for x in range(len(DavesList)):
                 print "car type:", DavesCarTypeList,"price:", DavesPricesList, ",", "supplier: DAVE"
        if(EricsList != None):
            EricsCarTypeList, EricsPricesList = zip(*EricsList)
            for x in range(len(EricsList)):
                print "car type:", EricsCarTypeList, "price:",EricsPricesList, ",", "supplier: ERIC"
        if(JeffsList != None):
            JeffsCarTypeList, JeffsPricesList = zip(*JeffsList)
            for x in range(len(JeffsList)):
                print "car type:", JeffsCarTypeList, "price:",JeffsPricesList, ",", "supplier: JEFF"


    else:
        if((DavesList != None) and (len(DavesList) !=0)):
            DavesCarTypeList, DavesPricesList = zip(*DavesList)
        if((EricsList != None) and (len(EricsList) !=0)):
            EricsCarTypeList, EricsPricesList = zip(*EricsList)
        if((JeffsList != None) and (len(JeffsList) !=0)):
            JeffsCarTypeList, JeffsPricesList = zip(*JeffsList)
        loopAround = 1
        while(loopAround <= 6):
            if(loopAround == 1):
                substring = '"STANDARD"'
            if(loopAround == 2):
                substring = '"EXECUTIVE"'
            if(loopAround == 3):
                substring = '"LUXURY"'
            if(loopAround == 4):
                substring = '"PEOPLE_CARRIER"'
            if(loopAround == 5):
                substring = '"LUXURY_PEOPLE_CARRIER"'
            if(loopAround == 6):
                substring = '"MINIBUS"'

            loopAround = loopAround + 1

            #checking if a supplier has the car type available
            if((DavesList != None) and (len(DavesList) !=0)):
                price_index1 = return_index(substring, DavesCarTypeList)
            if(EricsList != None and (len(EricsList) !=0)):
                price_index2 = return_index(substring, EricsCarTypeList)
            if((JeffsList != None) and (len(JeffsList) !=0)):
                price_index3 = return_index(substring, JeffsCarTypeList)

            #if available then get the corresponsing price
            numberOfCarTypesAvailable = 0
            if(price_index1 != None):
                price1 = DavesPricesList[price_index1]
                numberOfCarTypesAvailable = numberOfCarTypesAvailable + 1

            if(price_index2 != None):
                price2 = EricsPricesList[price_index2]
                numberOfCarTypesAvailable = numberOfCarTypesAvailable + 1

            if(price_index3 != None):
                price3 = JeffsPricesList[price_index3]
                numberOfCarTypesAvailable = numberOfCarTypesAvailable + 1

            if(numberOfCarTypesAvailable == 0):
                pricesList.append(None)
                cheapestCarTypes.append(substring)
                supplier.append(None)

            elif(numberOfCarTypesAvailable == 1):
                if(price1 != None):
                    minimum_price_for_car_type = price1
                    pricesList.append(price1)
                    supplier.append("DAVE")
                    cheapestCarTypes.append(substring)

                if(price2 != None):
                    minimum_price_for_car_type = price2
                    pricesList.append(price2)
                    supplier.append("ERIC")
                    cheapestCarTypes.append(substring)
                if(price3 != None):
                    minimum_price_for_car_type = price3
                    pricesList.append(price3)
                    supplier.append("JEFF")
                    cheapestCarTypes.append(substring)
            else:
                #find the first element that is not None and set
                #minimum_price_for_car_type to this value
                if(price1 != None):
                    minimum_price_for_car_type = price1

                elif(price2 != None):
                    minimum_price_for_car_type = price2

                elif(price3 != None):
                    minimum_price_for_car_type = price3


                #find the min price
                if(price1 != None and (price1 < minimum_price_for_car_type)):
                    minimum_price_for_car_type = price1
                if(price2 != None and (price2 < minimum_price_for_car_type)):
                    miuanimum_price_for_car_type = price2
                if(price3 != None and (price3 < minimum_price_for_car_type)):
                    minimum_price_for_car_type = price3


                if(minimum_price_for_car_type == price1):
                    pricesList.append(price1)
                    supplier.append("DAVE")
                    cheapestCarTypes.append(substring)
                if(minimum_price_for_car_type == price2):
                    pricesList.append(price2)
                    supplier.append("ERIC")
                    cheapestCarTypes.append(substring)
                if(minimum_price_for_car_type == price3):
                    pricesList.append(price3)
                    supplier.append("JEFF")
                    cheapestCarTypes.append(substring)
            price1 = None
            price2 = None
            price3 = None

        print "\nSearch Results:"
        sortedList = sortDescendingOrder2(cheapestCarTypes, pricesList, supplier)
        carList, pricesList, supplier = zip(*sortedList)
        for x in range(len(sortedList)):
            print "car type:", carList[x], "price:", pricesList[x], ",", "supplier:", supplier[x]
#Test cases --------------------------------------------------------------------
if(allOrOne == 2):
    print "Please hold on a moment...we are waiting for a response from",\
    "Dave's taxi base"
    makeBookingRequest(supplier1)

else:
    DavesList = makeBookingRequest(supplier1)

    timeResponse(supplier1)
    EricsList = makeBookingRequest(supplier2)

    timeResponse(supplier2)
    JeffsList = makeBookingRequest(supplier3)

    timeResponse(supplier3)
    if(DavesList != None):
        list(DavesList)
    if(EricsList != None):
        list(EricsList)
    if(JeffsList != None):
        list(JeffsList)
    filterResultsForAllSuppliers(DavesList, EricsList, JeffsList)
