year=int(input("Enter year\t"))
if year%4==0:
    print("{} is a leap year.".format(year))
else:
    print("{} is a lunar year.".format(year))
