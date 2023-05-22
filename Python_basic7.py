for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Couple,")
    elif num % 3 == 0:
        print("Boy,")
    elif num % 5 == 0:
        print("Girl,")
    else:
        print(num,end=",")
