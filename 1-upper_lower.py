print("I'm a Lower and Upper case Checker program ")

def checkUpper(str): 
    if ord(str) < 96: 
        return "Upper"
    return "Lower"

try: 
    checkInput = input("Enter to check: ")
    
    print("Checking...")
    print("{} is ".format(checkInput), checkUpper(checkInput))
except: 
    print("Only a single letter, not number")
