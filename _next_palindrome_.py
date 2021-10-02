'''
Author:Akhilesh Dhama
Date:16-Sept-2021
Purpose:Practice 4
'''
# For next palindrome
def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n
# To check whether it is a palindrome
def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__=="__main__":
    try:
        inp1=int(input("Enter the numbers you want check:\n"))
        lst1=[]
        print("enter nos")
        # To add the items in the list
        for i in range(inp1):        
                element=int(input(""))
                lst1.append(element)

        for i in range(inp1):
            print(f"Next palindrome for {lst1[i]} is {next_palindrome(lst1[i])}")
    except ValueError:
        print("Invalid input.please enter only integers")
         

