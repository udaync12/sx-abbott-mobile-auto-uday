# sx-abbott-mobile-auto-uday
Mobile Automation for General Store App

Requirements:
1. System: Windows 10 or above
2. Java 8 or above
3. IDE: Intellij (Can be imported to Eclipse)
4. Android Device or AVD 
5. MS Excel
6. Appium 

In order to run this automation suite:
1. Clone the repository to your local drive.
2. Start the Appium server and connect the device
3. Set JAVA_HOME and ANDROID_HOME
4. Launch the project from IntelliJ
5. Load the Maven dependenies (right click on pom.xml and Maven -> Reload Project)
6. Open the testng.xml file
7. Right click and Run the testng.xml

Notes:
1. Input data is read from the excel file from src/main/resources/ExcelInput/General_Store_Input_Master.xlsx
2. The first sheet in the excel has information about Device on which the test is to be run
3. Make the SKIP column blank for whichever row the device details are to be used.
4. The second sheet in the excel has information about Customer (e.g. Name, Country, Gender, Products, etc)
5. Make the SKIP column as blank for the row whose data needs to be used for the test
6. Adding 'x' and any value (even space) in the SKIP column means that the script will skip that row and read another row


