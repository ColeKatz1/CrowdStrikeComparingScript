import pandas
import re

def macsFilterLastLoginDate(macsMissingFromCSFilePath, CornellDatabaseFilePath, filterMonthNumber, filterYearNumber, date):
    macDevices = pandas.read_csv(macsMissingFromCSFilePath)
    macDevices = macDevices.drop(columns=macDevices.columns[:1],axis=1)
    macDevices.columns = ['ITS_Tag']

    macDf = pandas.read_excel(CornellDatabaseFilePath, sheet_name=['MAC CS Installed','MAC CS Not Installed']) #import excel file of Cornell's database of managed devices (this is not data from Crowdstrike, it is our own data)

    macInstalled = macDf.get('MAC CS Installed') #list of macs with CS installed (according to Cornell database, not CS)

    macsUsedInFilterMonth = []
    dateRegexFilterMonth = re.compile("" + filterYearNumber + "-" + filterMonthNumber + "-" + "\d{1,2}")


    for i in range(len(macInstalled['Last Check-in'])):
        if dateRegexFilterMonth.match(str(macInstalled['Last Check-in'][i])):
            macsUsedInFilterMonth.append(macInstalled['Asset Tag'][i])

    macsMissingFromOfficalCS = []

    macsUsedInFilterMonth = str(macsUsedInFilterMonth)



    for i in range(len(macDevices['ITS_Tag'])):
        if macDevices['ITS_Tag'][i] in macsUsedInFilterMonth:
            macsMissingFromOfficalCS.append(macDevices['ITS_Tag'][i])

    macsMissingFromOfficalCSDf = pandas.DataFrame(macsMissingFromOfficalCS)

    macsMissingFromOfficalCSDf.to_csv("" + filterMonthNumber + filterYearNumber + "_Macs_Missing_From_CS_Database_" + date + ".csv")


macsFilterLastLoginDate("C:/Users/colek/OneDrive/Desktop/New folder/Macs_Missing_From_CS_Database_8_11_22.csv", "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx", "07","2022","8_11_22")
