import pandas
import re

def createWindowsCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date): #CSHostFilePath is the file path on your computer to the csv downloaded from CS. For me, this is "C:/Users/colek/OneDrive/Desktop/New folder/CS_Host_Data_8_11_22.csv". 
                                                              #CornellDatabaseFilePath is the file path to the excel sheet which serves as our own database. For me, this is "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx"
                                                              #its important that the slashes are this direction "/" which I don't think is the default when copying the file path
                                                              #date is just the current date, this is for the file output
    
    crowdStrikeData = pandas.read_csv(CSHostFilePath) #import host management data downloaded from CS

    windowsCrowdStrikeData = crowdStrikeData[crowdStrikeData.Platform == 'Windows'] #only consider windows devices
    windowsOfficialCrowdStrikeList = windowsCrowdStrikeData['Hostname'].to_list() #creates list of windows device names (for example, PC210824)


    windowsDf = pandas.read_excel(CornellDatabaseFilePath, sheet_name=['Windows CS Installed','Windows CS Not Installed']) #import excel file of Cornell's database of managed devices (this is not data from Crowdstrike, it is our own data)

    windowsInstalled = windowsDf.get('Windows CS Installed') #list of windows devices with CS installed (according to Cornell's list)
    windowsUninstalled = windowsDf.get('Windows CS Not Installed') #list of windows devices without CS installed (according to Cornell's list)

    windowsRegex = re.compile("\D\D\d+") #this creates a regex used for windows devices (they are listed as PC210824 and we want them just as 210824 for example - this helps remove the "PC" part so we can compare between lists)

    for i in range(len(windowsOfficialCrowdStrikeList)): #goes through each device in the official CS database
        if windowsRegex.match(windowsOfficialCrowdStrikeList[i]): #checks for devices that match the regex (these are devices with PC******** with stars being numbers)
            windowsOfficialCrowdStrikeList[i] = re.sub(windowsRegex, windowsOfficialCrowdStrikeList[i][2:], windowsOfficialCrowdStrikeList[i]) #this will remove the "PC" part so the devices can be compared between lists

    windowsInstalledList = windowsInstalled['ComputerName'] #this gets the device names from Cornell's list of devices with CS installed

    for i in range(len(windowsInstalledList)): #this is doing the same thing where we remove the "PC" part so its just the device tag - this allows for better comparison across all lists
        if windowsRegex.match(str(windowsInstalledList[i])):
            windowsInstalledList[i] = re.sub(windowsRegex, windowsInstalledList[i][2:], windowsInstalledList[i])

    windowsUninstalledList = windowsUninstalled['Computer_Name'].to_list() #creates list of all windows in Cornell's list that we beleive don't have CS installed

    #important note: in the excel file, under "Windows CS Not Installed", there are two columns with the name "Computer Name". We want the 6th column so I changed this column name to "Computer_Name" so just added an underscore

    windowsToBeAddedToOfficialCS = []

    for i in range(len(windowsUninstalledList)): #goes through Cornell's list of windows without CS
        for j in range(len(windowsOfficialCrowdStrikeList)): #goes through CrowdStrike's list of windows devices
            if str(windowsUninstalledList[i]) == str(windowsOfficialCrowdStrikeList[j]): #checks for a match between these lists
                windowsToBeAddedToOfficialCS.append(windowsUninstalledList[i]) #if there is a match, add the device tag to the list

    windowsToBeAddedToOfficialCSDf = pandas.DataFrame(windowsToBeAddedToOfficialCS) #this is the list of devices that Cornell says do not has CS installed, but they are in the CS host management database




    basicRegex = re.compile("\D+") #creates a regex that will be used to remove devices with names like "Tony's Laptop"
    windowsMissingFromOfficalCS = []

    for i in range(len(windowsInstalledList)): #goes through all windows that Cornell has in their list of devices with CS installed
        if basicRegex.match(str(windowsInstalledList[i])): #this basically filters out the devices with names like "Rick's Laptop", we don't want these showing up in our list
            filler = 0
        else:    
            if str(windowsInstalledList[i]) not in windowsOfficialCrowdStrikeList: #checks if a device that Cornell has as having CS installed is missing from the CS host management database

                windowsMissingFromOfficalCS.append(windowsInstalledList[i]) #adds those missing devices to a list

    windowsMissingFromOfficalCSDf = pandas.DataFrame(windowsMissingFromOfficalCS)

    windowsMissingFromOfficalCSDf.to_csv("Windows_Missing_From_CS_Database_" + date + ".csv")
    windowsToBeAddedToOfficialCSDf.to_csv("Windows_That_Should_Have_CS_" + date + ".csv")
