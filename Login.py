from projectMenu import projectmenu
def login():
    try:
        fileObj = open("userinfo.txt", 'r')
    except Exception as a:
        print(a)
    else:
        print("\n============== Login Form ===============\n")
        print("Please Enter Your Email: ", end='')
        maill = input()
        print("Please Enter Your Password: ", end='')
        password = input()
        users = fileObj.readlines()
        for i in users:
            userinfo = i.strip("\n")
            finalinf = userinfo.split(":")
            if finalinf[3]==maill and finalinf[4]== password:
                print(f"\n===== User '{finalinf[1]}' Loged in successfully =====\n")
                projectmenu(finalinf[0])
                break
        else:
            print("\n===== User not found =====\n")
            login()
        fileObj.close()
