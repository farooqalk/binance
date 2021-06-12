import os, sys



confirmationString = str(input('This Will Kill Tasks Including Any Chrome.exe Process/es. Yes/no? ')).lower()
if((confirmationString == "yes" ) or (confirmationString == "y")):
    try:
        os.system("taskkill /im chrome.exe /f")
        print("Killed All Chrome Processes")
    except:
        print("An Unexpected Error Occured. Couldn't Free RAM")
    
else:
    print("Did Not Free Any Ram. Exitting...")
    sys.exit()