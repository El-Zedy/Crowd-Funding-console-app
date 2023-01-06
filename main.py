from Login import login
from Register import regestration

def logOrRegister():
    print("\n============ Welcome To Crowd-Funding =========== \n")
    while True:
        print("==== Please Choose ====: \n'1' for (Register)\n'2' for (Login)\n'3' for (Exit): ", end='')
        choice = input()
        if choice == "1":
            regestration()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\n=== See You Soon... :) ===\n")
            break
        else:
            print("\n=== Please Enter a Vaild Input! ===\n")
            continue
logOrRegister()