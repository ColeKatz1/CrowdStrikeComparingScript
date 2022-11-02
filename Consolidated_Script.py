from Windows_List import createWindowsCSVFiles
from Mac_Lists import createMacCSVFiles
from List_Filters import windowsFilterLastLoginDate
from List_Filters_Mac import macsFilterLastLoginDate


def consolidatedScript(CSHostFilePath, CornellDatabaseFilePath, date, filterMonth, filterMonthAsNumber, filterYear): #filterMonth would be "Jul" for example. filterMonthAsNumber would be "07" for July
    createWindowsCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date)
    createMacCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date)
    windowsFilterLastLoginDate("Windows_Missing_From_CS_Database_" + date +".csv", CornellDatabaseFilePath, filterMonth, filterYear, date)
    macsFilterLastLoginDate("Macs_Missing_From_CS_Database_" + date + ".csv", CornellDatabaseFilePath, filterMonthAsNumber,filterYear,date)

    
    
#Here is an example of how I would run this on my computer:
#The code belows gives all output files. You would replace some of the inputs on your computer to have the correct file paths.
#consolidatedScript("C:/Users/colek/OneDrive/Desktop/New folder/CS_Host_Data_8_11_22.csv","C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx","9_10_22","Jul","07","2022")

