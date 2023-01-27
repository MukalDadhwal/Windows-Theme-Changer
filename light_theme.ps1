# changes windows theme to aero(light)

start-process -filepath "C:\Windows\Resources\Themes\aero.theme"; timeout /t 1;taskkill /im "systemsettings.exe" /f
