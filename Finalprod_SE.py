#Sinclaire Hoyt
#Software Eng. Project 1



#Import all needed modules 
import yfinance as yf

import pandas as pd

from sense_emu import SenseHat

from stocksymbol import StockSymbol

import random

import csv

from random import randrange

sense = SenseHat()


#define first search by symbol function
def search_by_symbol():
  positive = "+"
  negative = "-"
  perc = "%"
  ticker = input('Enter your Stock Symbol: ')
#now we start to define everything for our math 
  stock = yf.Ticker(ticker).info
  symbol = stock['symbol']
  new_price = stock['currentPrice']
  old_price = stock['regularMarketPreviousClose']
  new_estimate = round(new_price, 2)
  new_estimate_str = str(new_estimate)
  old_estimate = round(old_price, 2)
  old_estimate_str = str(old_estimate)
  actual_change = round(new_estimate - old_estimate,2)
  actual_change_str = str(actual_change)
  percentage_change = round((actual_change/old_estimate) * 100,2)
  percent_change_str = str(percentage_change)
#
#sense hat and print messages are now beig coded
  sense_symbol = "Stock Symbol:"
  print('\n')
  sense.show_message(symbol, text_colour=[255,0,0])
  print('Stock Symbol:', symbol)
  sense.show_message(new_estimate_str, text_colour=[255,0,0])
  print('New Price:', new_estimate_str)
#
  if actual_change > 0:
      ac_to_string = str(actual_change)
      sense.show_message(positive+ac_to_string, text_colour=[255,0,0])
      print("Actual Change:",positive+ac_to_string)
  elif actual_change < 0:
      sense.show_message(actual_change_str, text_colour=[255,0,0])
      print('Actual Change: ', actual_change_str)
  else:
      sense.show_message(actual_change_str, text_colour=[255,0,0])
      print('Actual Change:', actual_change_str)
#
  if percentage_change > 0:
      c_to_string = str(percentage_change)
      sense.show_message(positive+c_to_string+perc,text_colour=[255,0,0])
      print(" Change:",positive+c_to_string+perc)
  elif percentage_change < 0:
      sense.show_message(percent_change_str+perc,text_colour=[255,0,0])
      print(' Change: ', percent_change_str+perc)
  else:
      sense.show_message(percent_change_str+perc,text_colour=[255,0,0])
      print(' Change:', percent_change_str+perc)
#
  sense.show_message(old_estimate_str, text_colour=[255,0,0])
  print('Old Price:', old_estimate)
  print('\n')


#defining search by all function

def search_by_all():
   positive = "+"
   negative = "-"
   perc = "%"
# open the file in read mode
   filename = open('/Users/sinclairehoyt/Desktop/stock_info.csv', 'r')
 
# creating dictreader object
   file = csv.DictReader(filename)
 
# creating empty lists
   ticker = []
   name = []
   exchange = []
 
# iterating over each row and append
# values to empty list
   for col in file:
     ticker.append(col['Ticker'])
   list_count = len(ticker)
   # printing the symbol  list using loop
   for x in range(len(ticker)):
    print('Ticker:', ticker[x])
#math functions being coded in
    stock = yf.Ticker(ticker[x]).info
    symbol = stock['symbol']
    new_price = stock['currentPrice']
    old_price = stock['regularMarketPreviousClose']
    new_estimate = round(new_price, 2)
    new_estimate_str = str(new_estimate)
    old_estimate = round(old_price, 2)
    old_estimate_str = str(old_estimate)
    actual_change = round(new_estimate - old_estimate,2)
    percentage_change = round((actual_change/old_estimate) * 100,2)
#
#
    sense_symbol = "Stock Symbol:"
    print('\n')
    sense.show_message(symbol, text_colour=[255,0,0])
    print('Stock Symbol:', symbol)
    sense.show_message(new_estimate_str, text_colour=[255,0,0])
    print('New Price:', new_estimate)
#if statements for the math 
    if actual_change > 0:
       ac_to_string = str(actual_change)
       sense.show_message(positive+ac_to_string, text_colour=[255,0,0])
       print("Actual Change:",positive+ac_to_string)
    elif actual_change < 0:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change: ', actual_change)
    else:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change:', actual_change)
#
    if percentage_change > 0:
       c_to_string = str(percentage_change)
       sense.show_message(positive+c_to_string+perc, text_colour=[255,0,0])
       print("Change:",positive+c_to_string +perc)
    elif percentage_change < 0:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change: ', percentage_change +perc)
    else:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change:', percentage_change+perc)
#
    sense.show_message(old_estimate_str, text_colour=[255,0,0])
    print('Old Price:', old_estimate)
    print('\n')
    quit()
#first search by random function for DJIA
def search_by_randDOW():
   positive = "+"
   negative = "-"
   perc = "%"
# open the file in read mode
   filename = open('/Users/sinclairehoyt/Desktop/DJIA-Copy.csv', 'r')
 
# creating dictreader object
   file = csv.DictReader(filename)
 
# creating empty lists
   ticker = []
   
 
# iterating over each row and append
# values to empty list2
   for col in file:
    ticker.append(col['Ticker'])
 
# iterating over each row and append
   rando = random.choice(ticker)
 
   print('Ticker:', rando)
#defining everything for math for stock info

   stock = yf.Ticker(rando).info
   symbol = stock['symbol']
   new_price = stock['currentPrice']
   old_price = stock['regularMarketPreviousClose']
   new_estimate = round(new_price, 2)
   new_estimate_str = str(new_estimate)
   old_estimate = round(old_price, 2)
   old_estimate_str = str(old_estimate)
   actual_change = round(new_estimate - old_estimate,2)
   actual_change_str = str(actual_change)
   percentage_change = round((actual_change/old_estimate) * 100,2)
   percent_change_str = str(percentage_change)
#
#Start coding out the functions for the sense hat and print functions
   sense_symbol = "Stock Symbol:"
   print('\n')
   sense.show_message(symbol, text_colour=[255,0,0])
   print('Stock Symbol:', symbol)
   sense.show_message(new_estimate_str, text_colour=[255,0,0])
   print('New Price:', new_estimate)
#if statements for math 
   if actual_change > 0:
       ac_to_string = str(actual_change)
       sense.show_message(positive+ac_to_string, text_colour=[255,0,0])
       print("Actual Change:",positive+ac_to_string)
   elif actual_change < 0:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change: ', actual_change)
   else:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change:', actual_change)
#
   if percentage_change > 0:
       c_to_string = str(percentage_change)
       sense.show_message(positive+c_to_string+perc, text_colour=[255,0,0])
       print("Change:",positive+c_to_string +perc)
   elif percentage_change < 0:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change: ', percentage_change +perc)
   else:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change:', percentage_change+perc)
#
   sense.show_message(old_estimate_str, text_colour=[255,0,0])
   print('Old Price:', old_estimate)
   print('\n')

#functions for NASDAQ
def search_by_randNAS():
   positive = "+"
   negative = "-"
   perc = "%"
# open the file in read mode
   filename = open('/Users/sinclairehoyt/Desktop/stock_info copy-NASDAQ 2.csv', 'r')
 
# creating dictreader object
   file = csv.DictReader(filename)
 
# creating empty lists
   ticker = []
   
 
# iterating over each row and append
# values to empty list2
   for col in file:
    ticker.append(col['Ticker'])
 
# iterating over each row and append
   rando = random.choice(ticker)
 
   print('Ticker:', rando)
#defining everything for math for stock info

   stock = yf.Ticker(rando).info
   symbol = stock['symbol']
   new_price = stock['currentPrice']
   old_price = stock['regularMarketPreviousClose']
   new_estimate = round(new_price, 2)
   new_estimate_str = str(new_estimate)
   old_estimate = round(old_price, 2)
   old_estimate_str = str(old_estimate)
   actual_change = round(new_estimate - old_estimate,2)
   actual_change_str = str(actual_change)
   percentage_change = round((actual_change/old_estimate) * 100,2)
   percent_change_str = str(percentage_change)
#
#Start coding out the functions for the sense hat and print functions
   sense_symbol = "Stock Symbol:"
   print('\n')
   sense.show_message(symbol, text_colour=[255,0,0])
   print('Stock Symbol:', symbol)
   sense.show_message(new_estimate_str, text_colour=[255,0,0])
   print('New Price:', new_estimate)
#if statements for math 
   if actual_change > 0:
       ac_to_string = str(actual_change)
       sense.show_message(positive+ac_to_string, text_colour=[255,0,0])
       print("Actual Change:",positive+ac_to_string)
   elif actual_change < 0:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change: ', actual_change)
   else:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change:', actual_change)
#
   if percentage_change > 0:
       c_to_string = str(percentage_change)
       sense.show_message(positive+c_to_string+perc, text_colour=[255,0,0])
       print("Change:",positive+c_to_string +perc)
   elif percentage_change < 0:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change: ', percentage_change +perc)
   else:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change:', percentage_change+perc)
#
   sense.show_message(old_estimate_str, text_colour=[255,0,0])
   print('Old Price:', old_estimate)
   print('\n')




#final function definition for the NYSE
def search_by_randNYSE():
   positive = "+"
   negative = "-"
   perc = "%"
# open the file in read mode
   filename = open('/Users/sinclairehoyt/Desktop/NYSE_stocks.csv', 'r')
 
# creating dictreader object
   file = csv.DictReader(filename)
 
# creating empty lists
   ticker = []
   
 
# iterating over each row and append
# values to empty list2
   for col in file:
    ticker.append(col['Ticker'])
 
# iterating over each row and append
   rando = random.choice(ticker)
 
   print('Ticker:', rando)
#defining everything for math for stock info
   stock = yf.Ticker(rando).info
   symbol = stock['symbol']
   new_price = stock['currentPrice']
   old_price = stock['regularMarketPreviousClose']
   new_estimate = round(new_price, 2)
   new_estimate_str = str(new_estimate)
   old_estimate = round(old_price, 2)
   old_estimate_str = str(old_estimate)
   actual_change = round(new_estimate - old_estimate,2)
   actual_change_str = str(actual_change)
   percentage_change = round((actual_change/old_estimate) * 100,2)
   percent_change_str = str(percentage_change)
#
#Start coding out the functions for the sense hat and print functions
   sense_symbol = "Stock Symbol:"
   print('\n')
   sense.show_message(symbol, text_colour=[255,0,0])
   print('Stock Symbol:', symbol)
   sense.show_message(new_estimate_str, text_colour=[255,0,0])
   print('New Price:', new_estimate)
#if statements for math 
   if actual_change > 0:
       ac_to_string = str(actual_change)
       sense.show_message(positive+ac_to_string, text_colour=[255,0,0])
       print("Actual Change:",positive+ac_to_string)
   elif actual_change < 0:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change: ', actual_change)
   else:
       sense.show_message(actual_change, text_colour=[255,0,0])
       print('Actual Change:', actual_change)
#
   if percentage_change > 0:
       c_to_string = str(percentage_change)
       sense.show_message(positive+c_to_string+perc, text_colour=[255,0,0])
       print("Change:",positive+c_to_string +perc)
   elif percentage_change < 0:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change: ', percentage_change +perc)
   else:
       sense.show_message(percentage_change+perc, text_colour=[255,0,0])
       print('Change:', percentage_change+perc)
#
   sense.show_message(old_estimate_str, text_colour=[255,0,0])
   print('Old Price:', old_estimate)
   print('\n')




   
# Code for the Menu and Submenu Function. Each function will give the user a choice to choose which option they want to get stocks from. 
def mainmenu():
    while(True):
      print('1. DJIA')
      print('2. NASDAQ')
      print('3. NYSE')
      print('Q. Quit')
      option = input ('Select an option: ')
      if option == 'q' or option == 'Q':
          exit()
      elif option == '1':
          DJIA_submenu()
      elif option == '2':
          NASDAQ_submenu()
      elif option == '3':
          NYSE_submenu()
      else:
          print ('Please select an option between 1 - 3.')
#first submenu-DJIA
def DJIA_submenu():
  while(True):
      print('\n DJIA Options')
      print('1. Search by symbol')
      print('2. Display a random symbol')
      print('3. Display all symbols')
      print('R. Return to Main Menu')
      option = input('Select an option: ')
      if option == 'r' or option == 'R':
           return
      elif option == '1':
          search_by_symbol()
      elif option == '2':
           print('\n')
           search_by_randDOW()
      elif option == '3':
          print('\n')
          search_by_all()  
      else:
          print ('Please select an option between 1 - 3.')

#second submenu-NASDAQ
def NASDAQ_submenu():
  while(True):
      print('\n NASDAQ Options')
      print('1. Search by symbol')
      print('2. Display a random symbol')
      print('3. Display all symbols')
      print('R. Return to Main Menu')
      option = input('Select an option: ')
      if option == 'r' or option == 'R':
           return
      elif option == '1':
          search_by_symbol()   
      elif option == '2':
         print('\n')
         search_by_randNAS()
      elif option == '3':
          print('\n')
          search_by_all() 
      else:
          print ('Please select an option between 1 - 3.')

#Final submenu-NYSE
def NYSE_submenu():
  while(True):
      print('\n NYSE Options')
      print('1. Search by symbol')
      print('2. Display a random symbol')
      print('3. Display all symbols')
      print('R. Return to Main Menu')
      option = input('Select an option: ')
      if option == 'r' or option == 'R':
           return
      elif option == '1':
          search_by_symbol()
      elif option == '2':
          print('\n')
          search_by_randNYSE()
      elif option == '3':
          print('\n')
          search_by_all() 
      else:
          print ('Please select an option between 1 - 3.')



  # Begin Main Code

mainmenu()






