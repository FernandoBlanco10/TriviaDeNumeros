import json
import requests

def trivia_fetch(n):
    
  url = f"http://numbersapi.com/{n}?json" 
  response = requests.get(url)
  trivia = response.json()
  return  trivia

def main():
  print("Hello learners!")
  
  n = input("Digite el numero del que quiera conocer informacion: ")
  print(trivia_fetch(n))

if __name__=="__main__":
  main()