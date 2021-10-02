'''
Author:Akhilesh Dhama
Date:8-Sept-2021
Purpose:Practice
'''
# to get the time
def gettime():
    import datetime
    return datetime.datetime.now()

# to log the diet or activity of patient
def log():
        print("Choose your patient")
        patient = int(input("1.Mavi\n 2.Avdhesh\n 3.Aman "))
        con = 1
        if(patient==1):
            while(con==1):
             print("What dou you wanna log in for Mavi?")
             choice = int(input("1.diet\n 2.activity"))
             if(choice==1):
                f = open("mavi diet.py","a")
                data = input("What Mavi has eaten?")
                f.write(str([str(gettime())]) + " " + data + "\n")
                f.close()
             else:
                f = open("mavi act.py", "a")
                data = input("what activity carried out by him?")
                f.write(str([str(gettime())]) + " " + data + "\n")
                f.close()
             con = int(input("Do you want to log more for Mavi? \n1. Yes \n2. No"))
        elif(patient==2):
            while (con == 1):
                print("What dou you wanna log in for Avdhesh?")
                choice = int(input("1.diet\n 2.activity"))
                if (choice == 1):
                    f = open("avdh diet.py", "a")
                    data = input("What Avdhesh has eaten?")
                    f.write(str([str(gettime())]) + " " + data + "\n")
                    f.close()
                else:
                    f = open("avdh act.py", "a")
                    data = input("what activity carried out by him?")
                    f.write(str([str(gettime())])+ " "+data+"\n")
                    f.close()
                con = int(input("Do you want to log more for Avdhesh? \n1. Yes \n2. No"))
        elif(patient==3):
            while (con == 1):
                print("What dou you wanna log in for Aman?")
                choice = int(input("1.diet\n 2.activity"))
                if (choice == 1):
                    f = open("aman diet.py", "a")
                    data = input("What Aman has eaten?")
                    f.write(str([str(gettime())])+ " "+ data+"\n")
                    f.close()
                else:
                    f = open("aman act.py", "a")
                    data = input("what activity carried out by him?")
                    f.write(str([str(gettime())]) + " " + data + "\n")
                    f.close()
                con = int(input("Do you want to log more for Aman? \n1. Yes \n2. No"))

# to retrieve the activity or diet done by patient
def retrive():
      con = 1
      while (con == 1):
        print("Choose your patient")
        patient = int(input("1.Mavi\n 2.Avdhesh\n 3.Aman "))
        if (patient == 1):
                print("What dou you wanna retrieve for Mavi?")
                choice = int(input("1.diet\n 2.activity"))
                if (choice == 1):
                    f = open("mavi diet.py", "r")
                    for line in f:
                        print(line,end="")
                    f.close()
                else:
                    f = open("mavi act.py", "r")
                    for line in f:
                        print(line,end="")
                    f.close()
        elif (patient == 2):
                print("What dou you wanna retrieve for Avdhesh?")
                choice = int(input("1.diet\n 2.activity"))
                if (choice == 1):
                    f = open("avdh diet.py", "r")
                    for line in f:
                        print(line,end="")
                    f.close()
                else:
                    f = open("avdh act.py", "r")
                    for line in f:
                        print(line,end="")
                    f.close()
        elif (patient == 3):
                print("What dou you wanna retrieve for Aman?")
                choice = int(input("1.diet\n 2.activity"))
                if (choice == 1):
                    f = open("aman diet.py", "r")
                    for line in f:
                        print(line,end="")
                    f.close()
                else:
                    f = open("aman act.py", "r")
                    for line in f:
                        print(line,end="")
                    f.close()
        con = int(input("\nDo you want to retrieve any more? \n1. Yes \n2. No"))

if __name__=="__main__":
    print("Welocome to the Dhama Health Care Management System")
    con = 1
    while(con==1):
        print("kya karna chahiyenge aap?\n 1.Log\n 2.Retrieve")
        a = int(input())
        if(a==1):
            log()
        elif(a==2):
            retrive()
        elif(a==3):
            exit()
        else:
            print("invalid input,please try again")
        con=int(input("Do you wanna proceed\n 1.Yes 2.No 'Exit'"))




