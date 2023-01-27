# Windows-Theme-Changer
simple python project to automatically change windows theme according to daytime and nighttime

my preference(you can change it to add yours) -> <br>
6 - 18 : light theme <br>
18 - 6(next day): dark theme

## Libraries used
***
- subprocess : used to run powershell scripts 
- datetime : used to get current datetime

## Usage
***
Put the file ```run.bat``` at  ```C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup``` to run the script on startup

## Extra note
***
change the variable filePath in windows_theme_changer to your folder path where your are running the script
and same in run.bat as well