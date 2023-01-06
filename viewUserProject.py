def viewUserProjects(uId):

    try:
        userProjects = open("projectInfo.txt", "r")
    except Exception as exc:
        print(exc)
    else:
        projects=userProjects.readlines()
        print("\n== Available Projects ==\n")
        count = 1
        for project in projects:
            uProjects = project.strip("\n")
            uProjectsinfo = uProjects.split(":")
            if uProjectsinfo[0] == uId:
                sData = f"Project {count} Name Is: {uProjectsinfo[1]}"
                print(sData)
                count = count + 1
        userProjects.close()
