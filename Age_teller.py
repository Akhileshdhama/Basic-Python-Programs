'''
Author:Akhilesh Dhama
Date:15-Sept-2021
Purpose:Practice 1
'''

while True:
    yearage=int(input("Enter your Age or Year of birth\n"))
    isyear=False
    isage=False
    if len(str(yearage))==4:
        isyear=True
    else:
        isage=True
    if yearage<1900 and isyear:
        print("You are the oldest alive\n")
        exit()
    if yearage>2021:
        print("you are not yet born\n")
    if isage:
        yearage=2021-yearage
    print(f"You will be 100 years old in {yearage+100} ")
    interestedyear = int(input("Enter the year you want to know your age in\n"))
    print(f"you will be {interestedyear-yearage} years old in {interestedyear}")


