To run this on your own computer:

First, download all files from github by clicking the green code button and then clicking "Download Zip".

<img width="461" alt="Screen Shot 2022-11-08 at 1 56 48 AM" src="https://user-images.githubusercontent.com/84477747/200496033-f1000731-eba3-4140-aa9e-d63f6b274d1f.png">

Next, you will need an IDE. For example, you can download visual studio code. https://code.visualstudio.com/download.

Then, right click the consolidated_script.py file and click "Open with visual studio code".

<img width="595" alt="Screen Shot 2022-11-08 at 2 00 48 AM" src="https://user-images.githubusercontent.com/84477747/200496350-2a3fe523-73c8-40b0-9ee9-d15b5ea26e12.png">

Then, click open folder (you can get here by clicking the files icon in the top left of visual studio code). Select the downloaded folder with all the python files in it as your folder. 

<img width="326" alt="Screen Shot 2022-11-08 at 2 01 16 AM" src="https://user-images.githubusercontent.com/84477747/200496486-042bcb3b-02b0-4c90-b05f-664915e938c9.png">

The final step is to replace the file paths and other inputs in the consolidatedScript function and then run the script! You run the script by clicking this icon in the top right.

<img width="119" alt="Screen Shot 2022-11-08 at 2 02 51 AM" src="https://user-images.githubusercontent.com/84477747/200496641-56c8b0ba-c089-4c8d-ad29-4dacde3d057e.png">

It should output the .csv files in the folder!

Explanation of files:

1. Windows_List.py - This file creates the function createWindowsCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date). 
There are 3 arguments/inputs for this function. The first is the file path on your computer to the host management file downloaded from CS. 
The second input, CornellDatabaseFilePath, is to the excel spreadsheet on your computer with our own data. Lastly, the date is just the current date for the file output name.
When run with these arguments, this function outputs two csv files. One contians a list of the ITS tags with devices missing from CS and the other contains a list of devices that are in CS, but we have them in our list as not having CS.
These .csv files are used later with the filtering functions.
Importantly, this function only deals with windows devices in the lists.

2. Mac_Lists.py - This file creates the function createMacCSVFiles(CSHostFilePath, CornellDatabaseFilePath, date).
The arguments and purpose are the same as above, but this function only deals with mac devices in the lists.
The output is again 2 .csv files.

3. List_Filters_Mac.py - This file creates the function macsFilterLastLoginDate(macsMissingFromCSFilePath, CornellDatabaseFilePath, filterMonthNumber, filterYearNumber, date).

The first input, macsMissingFromCSFilePath is the file path to one of the two .csv files output by Mac_Lists.py. The name of that file will be "Macs_Missing_From_CS_Database_" + date + ".csv" with date being whatever was input.
Next, CornellDatabaseFilePath is the same file path as in the past two functions.
filterMonthNumber and filterYearNumber allow filtering for a last login date. For example, 07 and 2022 would filter for devices who have a last login during July of 2022.
Finally, date is just the current date as before which is used for the output file names
Again, this function only deals with the macs

4. List_Filters.py - This file creates the function windowsFilterLastLoginDate(WindowsMissingFromCSFilePath, CornellDatabaseFilePath, filterMonth, filterYear, date)

The first input is the same as above but the name of the file will be "Windows_Missing_From_CS_Database_" + date + ".csv" with date being whatever was input.
CornellDatabaseFilePath is the same as above (excel spreadsheet)
filterMonth will have a different format as above according to the data. This means that July would be input as "Jul". August would be "Aug". I would check the data to ensure you enter the filterMonth in the correct format
filterYear is the same as above, probably "2022". Another important note is that these should be input as strings. You can follow the format shown at the bottom of the files where I input a sample function
Finally, date is the same as above

5. Consolidated_Script.py - This file imports the 4 functions above and allows you to run them in this cleaner environment without a bunch of code making it difficult to read what is going on.

