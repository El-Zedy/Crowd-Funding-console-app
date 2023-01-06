import re
from datetime import datetime

def checkMbile(m):
    pat = r'01[0-9]{9}$'
    if re.fullmatch(pat,m):
        return True
    else:
        return False
#------------------------------------------------------------#
def checkmail(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat,s):
        return True
    else:
        return False
#--------------------------------------------------------------#
def checkInputs(i):
    if ((not i.isspace()) and (i.isalpha())):
        vaildName = i
        return True
    else:
        return False
#-----------------------------------------------------------------#
def validPassword(p):
    if (len(p) > 6 and len(p) < 15):
        lowerCase = False
        upperCase = False
        num = False
        special = False
        for char in p:
            if(char.isdigit()):
                num = True
            if(char.islower()):
                lowerCase = True
            if (char.isupper()):
                upperCase = True
            if (not char.isalnum()):
                special = True

        return num and lowerCase and upperCase and special
    else:
        return False
#-----------------------------------------------------------------#
def passwordmatches(p1,p2):
    if p1 == p2:
        return True
    else:
        return False
#-----------------------------------------------------------------#

#print(validDate('02-12-2023'))
