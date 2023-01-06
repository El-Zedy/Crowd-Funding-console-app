from validation import *

def firstName():
    while True:
        print("Please Enter Your First Name: ", end='')
        firstName = input()
        if checkInputs(firstName) :
            return firstName
        else:
            print("\n== Error! Names Must Be Valid String Only ==\n")
            continue
    ######
def lastName():
    while True:
        print("Please Enter Your Last Name: ", end='')
        lasName = input()
        if checkInputs(lasName) :
            return lasName
            break
        else:
            print("\n== Error! Names Must Be Valid String Only ==\n")
            continue
    #######
def passInput():
    while True:
        print("Please Enter Your Password: ", end='')
        password = input()
        if validPassword(password):
            global validPass
            validPass = password
            return validPass
            break
        else:
            print("\n== Error! Use at least 6 characters. Use a mix of letters (uppercase and lowercase), numbers, and symbols. ==\n")
            continue
##########################

def confirmpassInput():
    while True:
        print("Please Confirm Your Password: ", end='')
        cpassword = input()
        if validPassword(cpassword) and passwordmatches(cpassword, validPass):
            return cpassword
            break
        else:
            print("\n== Error! Invalid or not match password ==\n")
            continue
##############

def mailInput():
    while True:
        print("Please Enter Your Email: ", end='')
        mail = input()
        if checkmail(mail) :
            return mail
            break
        else:
            print("\n== Error! Please Enter a Right Email Format, EX: t@example.com ==\n")
            continue
########
def mobileInput():
        while True:
            print("Please Enter Mobile: ", end='')
            mobile = input()
            if checkMbile(mobile) :
              return mobile
              break
            else:
                print("\n== Error! Must Be Egyptian Phone Numbers ==\n")
                continue
def uId():
    with open(r"userinfo.txt", 'r') as deta:
        x = len(deta.readlines())
        return x+1

def regestration():
    print("\n============== Register Form ===============\n")
    try:
        fileObj = open("userinfo.txt", 'a' )
    except Exception as a:
        print(a)
    else:
        userInfo = f"{uId()}:{firstName()}:{lastName()}:{mailInput()}:{passInput()}:{confirmpassInput()}:{mobileInput()}\n"
        fileObj.write(userInfo)
        fileObj.close()
    print(f"\n=== Registered successfully ===\n")