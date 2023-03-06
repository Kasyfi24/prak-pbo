#121140220
#RB

username = "Piton24"
password = "apaaja123"

for i in range(5):

    input_username = input("Input Username : ")
    input_password = input("Input Password : ")
    if input_username == username and input_password == password:
        print("login Successfull!")
        break
    else:
        print("Wrong username or password, try again?")
else:
    print("Your account has been locked, try again for 5 minutes")