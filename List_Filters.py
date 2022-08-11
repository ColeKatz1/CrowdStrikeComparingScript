import pandas
import re


def windowsFilterLastLoginDate(WindowsMissingFromCSFilePath, CornellDatabaseFilePath, filterMonth, filterYear, date):
    devices = pandas.read_csv(WindowsMissingFromCSFilePath)

    devices = devices.drop(columns=devices.columns[:1],axis=1)

    devices.columns = ['ITS_Tag']
    windowsDf = pandas.read_excel(CornellDatabaseFilePath, sheet_name=['Windows CS Installed','Windows CS Not Installed']) #import excel file of Cornell's database of managed devices (this is not data from Crowdstrike, it is our own data)
    windowsInstalled = windowsDf.get('Windows CS Installed') #list of windows devices with CS installed (according to Cornell's list)
    windowsRegex = re.compile("\D\D\d+") #this creates a regex used for windows devices (they are listed as PC210824 and we want them just as 210824 for example - this helps remove the "PC" part so we can compare between lists)

    for i in range(len(windowsInstalled['ComputerName'])):
        if windowsRegex.match(str(windowsInstalled['ComputerName'][i])):
            windowsInstalled['ComputerName'][i] = re.sub(windowsRegex, windowsInstalled['ComputerName'][i][2:], windowsInstalled['ComputerName'][i])


    windowsUsedInFilterMonth = []
    dateRegex = re.compile("\D*\d*" + filterMonth + filterYear + "")

    for i in range(len(windowsInstalled['LastReportTime'])):
        if dateRegex.match(windowsInstalled['LastReportTime'][i]): 
            windowsUsedInFilterMonth.append(windowsInstalled['ComputerName'][i])

    windowsMissingFromOfficalCS = []

    for i in range(len(devices['ITS_Tag'])):
        if devices['ITS_Tag'][i] in windowsUsedInFilterMonth:
            windowsMissingFromOfficalCS.append(devices['ITS_Tag'][i])
            
    windowsMissingFromOfficalCSDf = pandas.DataFrame(windowsMissingFromOfficalCS)

    windowsMissingFromOfficalCSDf.to_csv("" + filterMonth + filterYear + "_Windows_Missing_From_CS_Database" + date + ".csv")


windowsFilterLastLoginDate("C:/Users/colek/OneDrive/Desktop/New folder/Windows_Missing_From_CS_Database_8_11_22.csv", "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx", "Jul","2022","8_11_22")
