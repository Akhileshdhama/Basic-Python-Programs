'''
Author:Akhilesh Dhama
Date:10-Sept-2021
Purpose:Practice
'''
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__== '__main__':
    name = input("Enter your name\n")
    cat=input(f'Choose the category\n'
              f'["business","entertainment","health","science","sports","technology"]\n')
    r = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&category={cat}&apiKey=ab982b2d900d4179af4b4fa90866bdea")
    m = json.loads(r.text)
    n = m["articles"]
    speak(f"Hello {name}")
    speak(f"Today's top {cat} headlines are")
    for articles in n:
        print(articles["title"])
        print(articles["url"])
        speak(articles["title"])
        speak("Moving on to the next news...listen carefully")
    speak("Thank you.That's it for Today")