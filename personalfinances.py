import calendar  
import matplotlib.pyplot as plt
import numpy as np
import shutil
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime


def get_crypto_data(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_24hr_change=true"

    response = requests.get(url)
    data = response.json()

    price_usd = data[symbol]["usd"]
    percent_change_24h = data[symbol]["usd_24h_change"]

    return price_usd, percent_change_24h

def show_crypto_info(symbol, name):
    price, percent_change = get_crypto_data(symbol)
    print(f"{name} Price: ${price:.2f}")
    print(f"Percentage Change in the Last 24 Hours: {percent_change:.2f}%")


def show_SP():
  #shows about SPICE
  url = "https://www.investing.com/indices/us-spx-500"
  response = requests.get(url)

  soup = BeautifulSoup(response.content, 'html.parser')

  # Separate the attributes with a comma
  price_element = soup.find("div", class_="text-5xl font-bold leading-9 md:text-[42px] md:leading-[60px] text-[#232526]")
  sp500_price = price_element.text

  print("S&P 500 Price:", sp500_price)


#Also add a function inside these showing functions which shows detailed info on the prices, 1yr change, volume, graph etc etc;
  


def randomn_quote():
  
  string_list = [
    "Despite everything, it's still you.",
    "Only the fearless made proceed. Brave ones, foolish ones. Both walk not the middle road.",
    "It is a beautiful day outside. Birds are singing, flowers are blooming.... On days like these, kids like you... should be burning in hell.",
    "I can't go to hell. I'm all out of vacation days.",
    "You have something called 'determination.' So as long as you hold on... so as long as you do what's in your heart... I believe you can do the right thing.",
    "I'm 19 years old and I've already wasted my entire life.",
    "Lie to yourself all the time. It makes you feel better.",
    '"Friendship" is just a hot person\'s way of making you their slave.',
    "But you didn't get this far by giving up, did you? That's right. You have something called 'determination'. So as long as you hold on, so as long as you do what's in your heart, I believe you can do the right thing.",
    "Never interact with attractive people. Unless you're 'one of them' they're just gonna take advantage of you."
  ]

  random_output = random.choice(string_list)
  print(random_output)



class User:
  def __init__(self, name, age, salary, rent, expenses, invest, portfolio):
    self.name = name
    self.age = age
    self.salary = salary
    self.rent = rent
    self.expenses = expenses
    self.invest = invest
    self.portfolio = portfolio
    
  def show_info(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Salary: {self.salary}")
    print(f"Rent: {self.rent}")
    print(f"Expenses: {self.expenses}")
    print(f"Invest: {self.invest}")
    print(f"Portfolio: {self.portfolio}")

def inputs():
    name = input("What is your name? ")
    age = input("What is your age? ")
    salary = input("What is your salary? ")
    rent = input("What is your rent? ")
    expenses = input("What are your expenses? ")
    invest = input("How much do you invest? ")
    portfolio = input("What is your portfolio? ")  

    return User(name, age, salary, rent, expenses, invest, portfolio) 


 
 
while True:
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y\n%H:%M:%S")
    
    print(current_time)
    print(" ")
    print("\tW E L C O M E   T O   Y O U R   P E R S O N A L   F I N A N C E   M A N A G E R ")

    print(" ")
    # randomn_quote()
    print(" ")
    print("Market Updates ")
    print(" ")

    show_crypto_info("bitcoin", "Bitcoin")
    print(" ")
    show_crypto_info("ethereum", "Ethereum")
    print(" ")

    user = inputs()
    
    

    review_choice = input("Do you want to review your information? (y/n) ")
    if review_choice == "y":
        user.show_info()
        edit_choice = input("\nDo you want to edit it? (y/n) ")
        if edit_choice == "y":
            user = inputs()
        elif edit_choice == "n":
            print("Okay.")
        else:
            print("Please enter y/n.")
    else:
        print("Okay, let's move on.")

    def save_user_info(user):
        with open("user_info.txt", "w") as file:
            file.write(f"Name: {user.name}\n")
            file.write(f"Age: {user.age}\n")
            file.write(f"Salary: {user.salary}\n")
            file.write(f"Rent: {user.rent}\n")
            file.write(f"Expenses: {user.expenses}\n")
            file.write(f"Invest: {user.invest}\n")
            file.write(f"Portfolio: {user.portfolio}\n")

    # After gathering user information and updating portfolio
    save_user_info(user)



    invest_choice = input("Do you want to invest this month? (y/n) ")
    if invest_choice == "y":
        print("[1] Bitcoin")
        print("[2] Ethereum")
        print("[3] Theter")
        print("[4] Dogecoin")
        print("[5] Solana")
        print("[6] Cardano")
        print("[7] Polygon")
        print("[8] Shiba inu")
        print("[9] Suggest me")
        
        crypto_choice = input("Enter your choice: ")
        
        if crypto_choice == "1":
            # Bitcoin
            print("You chose Bitcoin")
            print(" ")
            show_crypto_info("bitcoin", "Bitcoin")
            money_choice = float(input("How much do you want to invest in Bitcoin?"))
            if money_choice > 0:
                print("Funds added", money_choice, "in Bitcoin")

        elif crypto_choice == "2":
            # Ethereum
            print("You chose Ethereum")
            print(" ")
            show_crypto_info("ethereum", "Ethereum")
            money_choice = float(input("How much do you want to invest in Ethereum?"))
            if money_choice > 0:
                print("Funds added", money_choice, "in Ethereum")
        
        elif crypto_choice == "3":
                # Tether
                print("You chose Tether")
                print(" ")
                show_crypto_info("tether", "Tether (USDT)")
                money_choice = float(input("How much do you want to invest in Tether?"))
                if money_choice > 0:
                    print("Funds added", money_choice, "in Tether")

        elif crypto_choice == "4":
                # Dogecoin
                print("You chose Dogecoin")
                print(" ")
                show_crypto_info("dogecoin", "Dogecoin")
                money_choice = float(input("How much do you want to invest in Dogecoin?"))
                if money_choice > 0:
                    print("Funds added", money_choice, "in Dogecoin")

        elif crypto_choice == "5":
                # Solana
                print("You chose Solana")
                print(" ")
                show_crypto_info("solana", "Solana")
                money_choice = float(input("How much do you want to invest in Solana?"))
                if money_choice > 0:
                    print("Funds added", money_choice, "in Solana")

        elif crypto_choice == "6":
                # Cardano
                print("You chose Cardano")
                print(" ")
                show_crypto_info("cardano", "Cardano")
                money_choice = float(input("How much do you want to invest in Cardano?"))
                if money_choice > 0:
                    print("Funds added", money_choice, "in Cardano")

        elif crypto_choice == "7":
                # Polygon
                print("You chose Polygon")
                print(" ")
                show_crypto_info("matic-network", "Polygon (MATIC)")
                money_choice = float(input("How much do you want to invest in Polygon?"))
                if money_choice > 0:
                    print("Funds added", money_choice, "in Polygon")

        elif crypto_choice == "8":
                # Shiba Inu
                print("You chose Shiba Inu")
                print(" ")
                show_crypto_info("shiba-inu", "Shiba Inu")
                money_choice = float(input("How much do you want to invest in Shiba Inu?"))
                if money_choice > 0:
                    print("Funds added", money_choice, "in Shiba Inu")


        elif crypto_choice == "9":
            print("You chose to be suggested")
            print(" ")
            print("Bitcoin (BTC) and Ethereum (ETH) are often favored for investment over other coins due to their longstanding presence, widespread recognition, market dominance, network security, mainstream adoption, and diverse use cases. They tend to offer more stability, liquidity, and institutional interest compared to many other cryptocurrencies in the market.")
            print("\nNOTE: The information provided is for educational purposes only and should not be considered as financial advice. Always conduct your own research and consult with a qualified financial advisor before making any investment decisions.")
        else:
            print("Please enter a valid choice")

    else:
        print("Try saving some money next month because investing is an effective way to put your money to work and potentially build wealth. Smart investing may allow your money to outpace inflation and increase in value. The greater growth potential of investing is primarily due to the power of compounding and the risk-return tradeoff.\n Visit https://www.investopedia.com for more info on how to get started")

    exit_choice = input("Do you want to exit the program? (y/n) ")
    if exit_choice.lower() == "y":
        print("Thank you for using the Personal Finance Manager. Goodbye!")
        break
 
  
  
  
  
