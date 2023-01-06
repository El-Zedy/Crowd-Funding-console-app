from viewUserProject import viewUserProjects
from editProject import getProjects

def deleteProject(uId):
    
    viewUserProjects(uId)
    projectsFromFile = getProjects()
    
    pName = input("\nPlease Select Project Name you Want To Delete: ")
    for project in projectsFromFile:
        usrProject = project.strip("\n")
        usrProject = usrProject.split(":")

        if usrProject[1] == pName and usrProject[0] == uId:
            projectsFromFile.remove(project)
            print(f"\n== Project '{pName}' Deleted successfully ==\n")
            break
    else:
        print(f"\n== Error! Something Went Wrong Or Project Is Not Found. ==\n")

    fileObj = open("projectInfo.txt", "w")
    fileObj.writelines(projectsFromFile)
    fileObj.close()
