from Windows_List import createWindowsCSVFiles
from Mac_Lists import createMacCSVFiles
from List_Filters import windowsFilterLastLoginDate
from List_Filters_Mac import macsFilterLastLoginDate


def consolidatedScript(CSHostFilePath, CornellDatabaseFilePath, date, filterMonth, filterMonthAsNumber, filterYear): #filterMonth would be "Jul" for example. filterMonthAsNumber would be "07" for July
    createWindowsCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date)
    createMacCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date)
    windowsFilterLastLoginDate("Windows_Missing_From_CS_Database_" + date +".csv", CornellDatabaseFilePath, filterMonth, filterYear, date)
    macsFilterLastLoginDate("Macs_Missing_From_CS_Database_" + date + ".csv", CornellDatabaseFilePath, filterMonthAsNumber,filterYear,date)

