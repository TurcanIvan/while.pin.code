# give the 3 user tries to enter pin code

SECRET_PIN = "1234"
tries      = 0


while tries < 3:
 #######enter & verify 1 time ##############       
    input_pin  = input("PIN: ")   
    if input_pin == SECRET_PIN:
        print("Access granted!!!")
        tries = 1000
    else:
        print("Access denied!!!")
        tries += 1
       

 ####enter & verify 1 time ################