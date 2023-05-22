username = "maryan"

password = "admin55"

input_username = input("Enter your username:\t ")

input_password = input("Enter your password:\t ")

if username==input_username:

    if password==input_password:

        print("login successful")

    else:

        print("password is incorrect")

else:

    print("username is incorrect")

if username!=input_username and password!=input_password:

    print("incorrect credentials")
