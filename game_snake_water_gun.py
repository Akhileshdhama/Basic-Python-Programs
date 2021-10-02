import random as r

print("WELCOME TO THE GAME")
list1 = ['s', 'w', 'g']
con='y'
count=0
wi=0
l=0
d=0
while(con=='y'):
  if(count<10):
    count = count + 1
    a=int(input("Press\n1-snake\n2-water\n3-gun\n"))
    b = r.choice(list1)
    if(a==1):
      if(b=='w'):
        print("YOU WON!!!\nJAO MAZZE KARO!!!")
        wi=wi+1
      elif(b=='g'):
        print("YOU LOSE!!!\nJAO MAR JAO!!!")
        l=l+1
      else:
        print("DRAW!!!\nTRY AGAIN!!!")
        d=d+1
    elif(a==2):
      if(b=='g'):
        print("YOU WON!!!\nJAO MAZZE KARO!!!")
        wi=wi+1
      elif(b=='s'):
        print("YOU LOSE!!!\nJAO MAR JAO!!!")
        l=l+1
      else:
        print("DRAW!!!\nTRY AGAIN!!!")
        d=d+1
    elif(a==3):
      if (b=='s'):
        print("YOU WON!!!\nJAO MAZZE KARO!!!")
        wi=wi+1
      elif (b=='w'):
        print("YOU LOSE!!!\nJAO MAR JAO!!!")
        l=l+1
      else:
        print("DRAW!!!\nTRY AGAIN!!!")
    else:
      print("INVALID ENTRY!!!\nTRY AGAIN!!!\nPLEASE SELECT ONLY CHOICES GIVEN ABOVE")
    print(10-count,"-ATTEMPS REMAINING")
    con = input("Y-PLAY AGAIN\nN-EXIT")
  elif(count==10):
    print("ALL ATTEMPTS EXHAUSTED\nSCORE!!!=", wi, "-", l, [d])
    if (wi>l):
      print("ULTIMATE WINNER!!!\nJAO MAVI P LAATH BAJAO")
    elif (wi<l):
      print("ULTIMATE LOSER!!!\nBETTER LUCK NEXT TIME")
    elif(wi==l):
      print("DRAW!!!")
    break
  con=input("DO YOU WANNA PLAY\nY-PLAY AGAIN\nN-EXIT")





