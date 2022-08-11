from Windows_List import createWindowsCSVFiles
from Mac_Lists import createMacCSVFiles
from List_Filters import windowsFilterLastLoginDate
from List_Filters_Mac import macsFilterLastLoginDate


createWindowsCSVFiles("C:/Users/colek/OneDrive/Desktop/New folder/CS_Host_Data_8_11_22.csv","C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx","8_12_22")
createMacCSVFiles("C:/Users/colek/OneDrive/Desktop/New folder/CS_Host_Data_8_11_22.csv","C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx","8_11_22")
windowsFilterLastLoginDate("C:/Users/colek/OneDrive/Desktop/New folder/Windows_Missing_From_CS_Database_8_11_22.csv", "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx", "Jul","2022","8_11_22")
macsFilterLastLoginDate("C:/Users/colek/OneDrive/Desktop/New folder/Macs_Missing_From_CS_Database_8_11_22.csv", "C:/Users/colek/OneDrive/Desktop/New folder/Compliance 2022-06_CrowdStrike.xlsx", "07","2022","8_11_22")
