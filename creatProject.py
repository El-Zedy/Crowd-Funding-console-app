from validation import *

def pTitle():
    while True:
        print("Please Enter Project Title: ", end='')
        pTitle = input()
        if checkInputs(pTitle):
            return pTitle
            break
        else:
            print("\n== Error! Title Must Be Valid String Only ==\n")
            continue

def pTotalTarget():
    while True:
        print("Please Enter Project Total Target: ", end='')
        totalTarget = input()
        if totalTarget.isnumeric():
            return totalTarget
            break
        else:
            print("\n== Error! Target Must Be Valid Numbers Only ==\n")
            continue

def getStartDate():
    print("Please Enter Project Start Date: ", end='')
    projdate = input()
    try:
        datetime.strptime(projdate, '%d-%m-%Y')
    except:
        print("\n== Incorrect data format, should be DD-MM-YYY ==\n")
        getStartDate()
    else:
        return projdate

def getEndDate():
    print("Please Enter Project End Date: ", end='')
    projdate = input()
    try:
        datetime.strptime(projdate, '%d-%m-%Y')
    except:
        print("\n== Incorrect data format, should be DD-MM-YYY ==\n")
        getEndDate()
    else:
        return projdate

def pDetails():
    print("Please Enter Project Details: ", end='')
    details = input()
    return details
#=====================================================================================

def createProject(uId):

    print("\n======= Create Project Form =======\n")
    createProjectData = f"{uId}:{pTitle()}:{pDetails()}:{pTotalTarget()}:{getStartDate()}:{getEndDate()}\n"
    try:
        fileObj = open("projectInfo.txt", 'a')
    except Exception as a:
        print(a)
        createProject(uId)
    else:
        fileObj.write(createProjectData)
        fileObj.close()
    print(f"\n=== Project Created successfully ===")
