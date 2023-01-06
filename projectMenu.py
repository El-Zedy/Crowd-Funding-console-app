from deleteProject import deleteProject
from creatProject import createProject
from viewAllProjects import listProjects
from editProject import editProject
from viewUserProject import viewUserProjects

def projectmenu(uId):
    print("\n=== Project Menu ==== ")
    while True:
        choice = input(
            "\n== Please Choose ==:\n(1) To 'Create' New Project\n(2) To 'List' All Projects\n(3) To 'List' Your Projects\n(4) To 'Edit' A Project\n(5) To 'Delete' A Project\n(6) To 'Log Out'\n")

        if choice == "1":
            createProject(uId)

        elif choice == "2":
            listProjects()

        elif choice == "3":
            viewUserProjects(uId)

        elif choice == "4":
            editProject(uId)

        elif choice == "5":
            deleteProject(uId)

        elif choice == "6":
            print("\n=== Logged Out successfully ===\n")
            break
        else:
            print("\n== Erorr! Please Enter A Valid Input ==\n")
            projectmenu(uId)
