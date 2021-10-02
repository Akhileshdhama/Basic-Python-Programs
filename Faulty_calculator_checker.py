'''
Author:Akhilesh Dhama
Date:16-Sept-2021
Purpose:Practice 8
'''

import random

# rohan's faulty table
def rohan_multiplication(table_no):
    table_list=[]
    for i in range(1,11):
        table_list.append(table_no*i)
    a=random.randint(2,7)   
    table_list[a]=table_list[a]+random.randint(1,9)   
    return table_list

# checker for rohan's table
def multiplication_checker(table_no,resullted_table):
    for i in range(1,11):
       if resullted_table[i-1]!=table_no*i:
            return print(f"Rohan has frauded you by faulty table with wrong ({i}:{resullted_table[i-1]})\nWhile actual one is ({i}:{table_no*i})")
    return print(f"Rohan's table correct,He is really a generous person")  

if __name__=="__main__":
    try:
        table=int(input("Enter the numbers of which table you wants to print:\n"))
        rohan_table=rohan_multiplication(table)
        print(rohan_table)
        check=int(input("Do you wanna check rohan's table.Is is correct or not?\nPress\n1.Check\n2.No\n"))
        if check==1:
            multiplication_checker(table,rohan_table)
        elif check==2:
            exit()
        else:
            print("Invalid Input.")

    except ValueError:
        print("Invalid Input.Please enter integers only")            

    