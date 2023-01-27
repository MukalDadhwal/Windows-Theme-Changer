from subprocess import Popen
from sys import stdout
from datetime import datetime

def runScript(file: str) -> None:
    """
        runs the file in powershell when executed
        Parameters:
            file: string file name
        Return:
            None
    """
    shellFile = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    filePath = f"D:\\Mukal\\Programming\\Powershell_Scripts\\{file}"
    file = Popen([shellFile, filePath], stdout=stdout)

    file.communicate()

currTime = datetime.now()

# dark theme time interval(00 am - 6 am )
# 1
zeroAMofCurrentDay = currTime.replace(hour=00, minute=0, second=0, microsecond=0)
sixAM = currTime.replace(hour=6, minute=0, second=0, microsecond=0)

# 2 (18 pm - 00 am)
sixPM = currTime.replace(hour=18, minute=0, second=0, microsecond=0)
zeroAMofNextDay = currTime.replace(hour=0, minute=0, second=0, microsecond=0, day=(currTime.day+1))

# light theme time interval(6am - 18pm)
eighteenPM = currTime.replace(hour=18, minute=0, second=0, microsecond=0)


if zeroAMofCurrentDay <= currTime < sixAM:
    runScript("dark_theme.ps1")
elif sixAM <= currTime < eighteenPM:
    runScript("light_theme.ps1")
else:
    runScript("dark_theme.ps1")