from Windows_List import createWindowsCSVFiles
from Mac_Lists import createMacCSVFiles
from List_Filters import windowsFilterLastLoginDate
from List_Filters_Mac import macsFilterLastLoginDate

#createWindowsCSVFiles creates two lists. One is a list of devices that should have CS installed but don't show up in CS host management
#The other is a list of devices that we have in our own database as not having CS installed, but they do show up in CS host management
createWindowsCSVFiles("C:/Users/colek/OneDrive/Desktop/New folder/CS_Host_Data_8_11_22.csv","C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx","8_12_22")
#this creates the same lists as above but for macs instead of windows
createMacCSVFiles("C:/Users/colek/OneDrive/Desktop/New folder/CS_Host_Data_8_11_22.csv","C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx","8_11_22")
#this filters for windows last active in a specified month
windowsFilterLastLoginDate("C:/Users/colek/OneDrive/Desktop/New folder/Windows_Missing_From_CS_Database_8_11_22.csv", "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx", "Jul","2022","8_11_22")
#this filters for macs last active in a specified month - the syntax of the month is slightly different (you put the month in number form like 07 for July)
macsFilterLastLoginDate("C:/Users/colek/OneDrive/Desktop/New folder/Macs_Missing_From_CS_Database_8_11_22.csv", "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx", "07","2022","8_11_22")
