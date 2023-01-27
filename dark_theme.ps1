# changes windows theme to themeA(dark)
# timeout /t 1;

start-process -filepath "C:\Windows\Resources\Themes\themeA.theme"; timeout /t 1;taskkill /im "systemsettings.exe" /f