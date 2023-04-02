from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.
auction_data={}
def addd(name,bid):
  auction_data[name]=bid
def compare(auction_data):
  max=0
  for i in auction_data:
    if auction_data[i]>max:
      max=auction_data[i]
      winner=i
      
  print(f"winner is {winner}")
      
    
  
  
  
#auction_data=[]

flag="yes"
while flag=="yes":
  name = input("what is your name? :")
  bid=int(input("what is your bid? :"))
  addd(name,bid)
  flag=input("Are there any other bidders? Type yes or no: ")
  if flag == "no":
    compare(auction_data)
  if flag == "yes":
    clear()
  

