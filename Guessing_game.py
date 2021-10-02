'''
Author:Akhilesh Dhama
Date:16-Sept-2021
Purpose:Practice 6
'''
import random

# Guessing game
if __name__=="__main__":
    try:
        mn=int(input("Enter first number:\n"))
        mx=int(input("Enter second number:\n"))
        n=int(input("Enter the no of players you want play:"))
        dict1={}
        for i in range(n):
            b=random.randint(mn,mx)
            player=input(f"Enter the name of player {i+1}:\n")
            m=0
            while True:
                m+=1
                guess=int(input("Please guess your number:\n"))
                if guess<b:
                    print("You guessed it wrong.Smaller than actual")
                elif guess>b:
                    print("You guessed it wrong.Greater than actual")
                else:
                    print(f"WOW!!!,You guessed it right in {m} number of guesses")
                    dict1.update({f"{player}":m})
                    print
                    break
        print(dict1)        
        Keymin = min(dict1, key=lambda x: dict1[x])
        list22=[]
        count=0
        for key,value in dict1.items():
            if value==min(dict1.values()):
                list22.append(key)
                count+=1
        if count>1:
            print(f"It's a tie between {list22}.I think you guys play again to decide or break up prize")
        else:   
            print(f"{Keymin} is the WINNER.\nWINNER WINNER NOTHING DINNER!!!")
    except ValueError:
        print("Invalid input.Please Try Again")



