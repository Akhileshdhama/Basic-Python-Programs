'''
Author:Akhilesh Dhama
Date:08-Sept-2021
Purpose:Practice 
'''
from datetime import datetime
import time
import winsound

# to log activity in file
def log1(file):
    with open("Health Log.txt", "a") as f:
        f.write(f"{datetime.now()}  {file}\n")
        f.close()

# sound alarm to notify about activity to be done using winsound
def water_1(file):
    winsound.PlaySound(f"'{file}.wav', {winsound.SND_LOOP}  {winsound.SND_ASYNC}")
    print(f"please do {file}\n")
    b=input(f"If completed Press 'D-DONE\n").upper()
    if(b=="D"):
        winsound.PlaySound(None, winsound.SND_PURGE)
        log1(file)
    while b != "D":
        print("----Invalid input! Try again----")
        b = input(f"If completed Press 'D-DONE\n").upper()
        if b == "D":
            winsound.PlaySound(None, winsound.SND_PURGE)
            print(f"please do {file}\n")
            log1(file)

if __name__ == '__main__':
  print("This works only for 9am-6pm")
  p=time.strftime('%H')
  while True:
    if('09'<p) and (p<'18'):
      while(1):
          time.sleep(10)
          water_1("water")
          break
      while(1):
          time.sleep(16)
          water_1("eyes")
          break
      while(1):
          time.sleep(22)
          water_1("physical")
          break
      time.sleep(5)

    else:
      print("It will work only for 9am-5pm, Please Try Again after 9am ")
      break





