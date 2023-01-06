
def listProjects():
    try:
        projobj = open("projectInfo.txt", "r")
    except Exception as exc:
        print(exc)
        return False
    else:
        projects = projobj.readlines()
        counter = 1
        print("\n ==== Projects List ==== \n")
        for i in projects:
            fileInfo = i.strip("\n")
            for x in fileInfo:
                progInfo = fileInfo.split(":")
                print(f"Project {counter} Info is:")
                print("------------------------------------")
                print(f"Project ID: {progInfo[0]}\nProject Title: {progInfo[1]}\nProject Details: {progInfo[2]}\nProject Target: {progInfo[3]}\nProject Dates: {progInfo[4]} To {progInfo[5]}\n")
                counter = counter + 1
                break
    projobj.close()
