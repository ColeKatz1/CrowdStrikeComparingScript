import pandas
import re
def createMacCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date): #CSHostFilePath is the file path on your computer to the csv downloaded from CS. For me, this is "C:/Users/colek/OneDrive/Desktop/New folder/CS_Host_Data_8_11_22.csv". 
                                                              #CornellDatabaseFilePath is the file path to the excel sheet which serves as our own database. For me, this is "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx"
                                                              #its important that the slashes are this direction "/" which I don't think is the default when copying the file path
                                                              #date is just the current date, this is for the file output
    crowdStrikeData = pandas.read_csv(CSHostFilePath) #import host management data downloaded from CS

    macCrowdStrikeData = crowdStrikeData[crowdStrikeData.Platform == 'Mac'] #only consider macs
    macOfficialCrowdStrikeList = macCrowdStrikeData['Hostname'].to_list() #gets hostnames of the macs from CS

    macDf = pandas.read_excel(CornellDatabaseFilePath, sheet_name=['MAC CS Installed','MAC CS Not Installed']) #import excel file of Cornell's database of managed devices (this is not data from Crowdstrike, it is our own data)

    macInstalled = macDf.get('MAC CS Installed') #list of macs with CS installed (according to Cornell database, not CS)
    macUninstalled = macDf.get('MAC CS Not Installed') #list of macs without CS installed (according to Cornell database, not CS)

    macInstalledList = macInstalled['Asset Tag'].to_list() #gets the asset tags of macs that Cornell has listed as having CS installed
    macUninstalledList = macUninstalled['Asset Tag'].to_list() #gets the asset tags of macs that Cornell has as listed as NOT having CS installed

    macRegex = re.compile("\D\D\D\d+") #creates regex that will be used to remove "MAC" and only keep the asset tag 

    for i in range(len(macOfficialCrowdStrikeList)): #goes through CS list of macs
        if macRegex.match(macOfficialCrowdStrikeList[i]): #checks if the regex matches
            macOfficialCrowdStrikeList[i] = re.sub(macRegex, macOfficialCrowdStrikeList[i][3:], macOfficialCrowdStrikeList[i]) #removes the "MAC or mac" to only keep asset tag so the lists can be compared

    macsToBeAddedToOfficialCS = []

    # checks for macs that apparently don't have CS but show up in the CS database

    for i in range(len(macUninstalledList)): #goes through list of macs that we have in our database as NOT having CS
        for j in range(len(macOfficialCrowdStrikeList)): #goes through the list of macs from official CS database
            if str(macUninstalledList[i]) == str(macOfficialCrowdStrikeList[j]): #checks if there is a match between lists
                macsToBeAddedToOfficialCS.append(macUninstalledList[i]) #adds devices to a new list if there is a match

    macsToBeAddedToOfficialCSDf = pandas.DataFrame(macsToBeAddedToOfficialCS) #list of macs that we have in our database as not having CS but they show up in the CS host management database

    basicRegex = re.compile("\D+") #creates regex that filters for device names like "Tom's Laptop" which we don't want to add to our list

    macsMissingFromOfficalCS = []

    #checks for macs that apparently have CS but do not show up in the official CS database

    for i in range(len(macInstalledList)): #goes through list of macs that we have in our database as having CS
        if basicRegex.match(str(macInstalledList[i])): #filters out the unwanted laptops - laptops with weird names
            filler = 0
        else:    
            if str(macInstalledList[i]) not in macOfficialCrowdStrikeList: #checks for devices that we say have CS installed but are missing from the CS host management database
                macsMissingFromOfficalCS.append(macInstalledList[i]) #adds devices missing from CS database to a new list

    macsMissingFromOfficalCSDf = pandas.DataFrame(macsMissingFromOfficalCS)


    macsMissingFromOfficalCSDf.to_csv("Macs_Missing_From_CS_Database_" + date + ".csv")
    macsToBeAddedToOfficialCSDf.to_csv("Macs_That_Should_Have_CS_" + date + ".csv")
