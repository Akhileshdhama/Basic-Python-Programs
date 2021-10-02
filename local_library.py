'''
Author:Akhilesh Dhama
Date:11-Sept-2021
Purpose:Practice 1
'''

# using OOPs
class library:
    def __init__(self,list_of_books,name_of_library):
        self.list_of_books=list_of_books
        self.name_of_library=name_of_library
        self.lended_book={}
        self.requested_book={}

    def displaybooks(self):
        print("Books present at the moment in Dhama library are given below:")
        for items in self.list_of_books:
            print(items)
        return f"We have only these books now\nIf you didn't find the desired book\nYou can request it from main menu."
    
    def lendbooks(self,user_name,book_name):
        if book_name not in self.lended_book.keys():
            self.lended_book.update({book_name:user_name})
            self.list_of_books.remove(book_name)
            print(f"You have lended {book_name} succesfully.ENJOY!!!")
        else:
            print(f"Book is already being used by {self.lended_book[book_name]}")
    
    def addbooks(self,new_book):
        self.list_of_books.append(new_book)
        print(f"Succesfully added the {new_book} to our library.Thank You!!!")
    
    def returnbooks(self,user_name,new_book):
        if new_book not in self.list_of_books:
            self.lended_book.pop(new_book)
            self.list_of_books.append(new_book)
            print(f"You have succesfully returned {new_book} to the library.Thank You!!!")
        else:
            print(f"Sorry you haven't lended this book till now.\n"
                  f"Books landed by you are: {self.lended_book[user_name]}")

    def requestbooks(self,user_name,book_name):
       self.requested_book.update({book_name:user_name})
       print(f"Thank You!!! We will notify when {book_name} will be available.\nTill then explore the available one.")

def system():
    try:
        value=True
        Dhama = library(
            ["Who moved my chesse", "The alchemist", "The monk who sold his ferrari", "Rich dad,Poor dad", "Quiet","The power of now"],
            "DHAMA LIBRARY")
        user_name = input("Enter your name:\n").capitalize()
        while True:
            print(f"Welcome {user_name} to The {Dhama.name_of_library}:\n"
                  f"For what you are here?\n"
                  f"Please let us know by press on the options given below:\n"
                  f"Press 1 to display the list of books\n"
                  f"Press 2 to lend the books\n"
                  f"Press 3 to add/donate the books\n"
                  f"Press 4 to return the books\n"
                  f"press 5 to request the books\n"
                  f"Press 6 to exit")
            choice=int(input())
            if choice==1:
                print(Dhama.displaybooks())
            elif choice==2:
                print(Dhama.displaybooks())
                while True:
                    book_name = input("Enter the name of book you wanna lend:\n").capitalize()
                    Dhama.lendbooks(user_name,book_name)
                    input1=int(input("Do you wanna lend more?\n1.Yes\n2.No\n"))
                    if input1==1:
                        continue
                    elif input1==2:
                        break
                    else:
                        print("Invalid input.TRY AGAIN!!!")
                        continue
            elif choice==3:
                while True:
                    new_book = input("Enter the name of the book you wanna donate/add:\n").capitalize()
                    Dhama.addbooks(new_book)
                    input1=int(input("Do you wanna add/donate more?\n1.Yes\n2.No\n"))
                    if input1==1:
                       continue
                    elif input1==2:
                        break
                    else:
                        print("Invalid input.TRY AGAIN!!!")
                        continue
            elif choice==4:
                new_book = input("Enter the name of the book you wanna return:\n").capitalize()
                Dhama.returnbooks(user_name,new_book)
            elif choice==5:
                book_name = input("Enter the name of the book you wanna request:\n").capitalize()
                Dhama.requestbooks(user_name,book_name)
            elif choice==6:
                break
            else:
                print("You have entered the wrong input.Please Try Again!!!")
                continue
    except:
       print("Error!!!")
       system()

if __name__=="__main__":   
    system()











