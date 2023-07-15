def getage():
    dof=[7,5,2023]
    dob=[]
    a=int(input("Please Entre your month of birth : "))
    b=int(input("Please Entre the day of your birth :"))
    year=int(input("Please entre your year of birth: "))
    dob.append(a)
    dob.append(b)
    dob.append(year)
    if dob[2]>dof[2]:
        print("Entre a valid year")
    elif dob[2]<dof[2]:
        yob= dof[2]-dob[2]
        print(yob)

        day=dof[1]-dob[1]

      
getage()
          