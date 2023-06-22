n = int(input("Enter Zigzag length "))

def ziggi_game(str):
    while True:  
        for i in range(1, 20+1):
            for j in range(1, 20+1):
                if(((i+j)%4==0) | (i==2) & (j%4==0)):
                    print("*", end=" ")
                else: 
                    print(" ", end=" ")
            print()  
ziggi_game(n)
