from viewUserProject import viewUserProjects
from creatProject import pTitle, pDetails, pTotalTarget,getEndDate,getStartDate

def getProjects():
    try:
        usrProjects = open("projectInfo.txt", "r")
    except Exception as exc:
        print(exc)
    else:
        projects = usrProjects.readlines()
        usrProjects.close()
        return projects
############################################

def editProject(uId):
    
    viewUserProjects(uId)
    projectsFromFile=getProjects()

    pName = input("\nPlease Select Project Name you Want To Edit: ")
    for line in projectsFromFile:

        usrProject = line.strip("\n")
        usrProject = usrProject.split(":")

        if usrProject[1] == pName and usrProject[0] == uId:
            inputToEdit = input("\n==== Please Choose ====\n'1' For Edit (Project Tittle)\n'2' For Edit (Project Details)\n'3' For Edit (Project Target)\n'4' For Edit (Start Date)\n'5' For Edit (End Date)\n")

            if inputToEdit == "1":
                newtittle = pTitle()
                usrProject[1] = newtittle
                print("\n== Project Title Upadted successfully ==\n")

            elif inputToEdit == "2":
                prjDetail = pDetails()
                usrProject[2] = prjDetail
                print("\n== Project Details Upadted successfully ==\n")

            elif inputToEdit == "3":
                prjTarget = pTotalTarget()
                usrProject[3] = prjTarget
                print("\n== Project Target Upadted successfully ==\n")

            elif inputToEdit == "4":
                prjStartDate = getStartDate()
                usrProject[4] = prjStartDate
                print("\n== Project Start Date Upadted successfully ==\n")

            elif inputToEdit == "5":
                 prjEndDate = getEndDate()
                 usrProject[5] = prjEndDate
                 print("\n== Project End Date Upadted successfully ==\n")

            else:
                print(f"\n== Error! Something Went Wrong Or Project Is Not Found. ==\n")
                break

            editedProj = ":".join(usrProject)
            editedProj = f"{editedProj}\n"
            prjIndex = projectsFromFile.index(line)
            projectsFromFile[prjIndex] = editedProj
            break


    fileObj = open("projectInfo.txt", "w")
    fileObj.writelines(projectsFromFile)
    fileObj.close()



