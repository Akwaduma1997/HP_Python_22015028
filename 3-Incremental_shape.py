while True: 
    try: 
        userInput = int(input("Enter number to be incremented to: "))
        i = 0
        while i < userInput + 1: 
            print("#"*i)
            i = i + 1
        break
    except:
        print("Only integer character is allowed, try again")
