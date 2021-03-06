#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:50:20 2017

@author: admin
"""

#
#import sqlite3
#
## create connection with database
#conn = sqlite3.connect('LeVinEmployee.db') #Insert with your location of database
#
#def login():
#    user_email = input("What is your Email? ")
#
#    with conn:
#        # creating a cursor that will execute commands against the db
#        cur = conn.cursor()
#
#        try:
#            while "@" not in user_email:
#                user_email = input("Please enter a valid email address: ")
#
#            cur.execute("SELECT Email FROM Employee WHERE (Email = '" + user_email + "')")
#            # runs the SQL command and assigns the result of the command to a cursor object called cursor
#            email_Info = cur.fetchone()  
#            # if any info retrieved then user entered email is in the database
#            if email_Info:
#                user_pass = input("What is your Password? ")
#                # find password entered by user in dataBase
#                cur.execute("SELECT Password FROM Employee WHERE (Email = '" + user_email + "')")
#                pass_Info = cur.fetchone()
#                pass_Info = pass_Info[0]
#                cur.execute("SELECT FirstName, LastName FROM Employee WHERE (Email = '" + user_email + "')")
#                name_Info = cur.fetchall()
#                
#                #checks to see if the password entered matches pass_Info taken from database
#                while user_pass != pass_Info:
#                    user_pass = input("Password incorrect, please try again: ")
#                #if the password is already correct it will then print a welcome message to the user
#                if user_pass == pass_Info:
#                    # Check if user entered password(user_pass) is the same as password in database(pass_info)
#                    # print Name of User
#                    for row in name_Info:
#                        return print("Welcome " + row[0] + " " + row[1]+ ".", end=' ')
#                                 
#        except ConnectionError:
#            return print("Connection Failed")
#
#        
#        
#def register():
#    with conn:
#        cur = conn.cursor()
#        try:
#            empID = input("To register a new employee, first enter his or her EmployeeID: ")  
#            stripEmpID = empID.strip()
#            #Checks if the variable is not equal to 4, if it isnt then it will force them to re-enter their information
#            while len(stripEmpID) != 4:
#                stripEmpID = input("Employee ID cannot be longer or shorter than 4 numbers and can only contain numbers, no letters. Please try again: ")
#            
#            #Checks if the variable is not in the form of digits only, if it isnt then it will force them to re-enter their information
#            while not stripEmpID.isdigit():
#                stripEmpID = input("Employee ID cannot be longer or shorter than 4 numbers and can only contain numbers, no letters. Please try again: ")
#            #if the length of the entry is 4 numbers then it will proceed to the rest of the registration form.    
#            if len(stripEmpID) == 4 and stripEmpID.isdigit():
#                with conn:
#        
#                    try:
#                        cur.execute("SELECT EmployeeID FROM Employee WHERE(EmployeeID ='" + stripEmpID + "')")
#                        checkEmpID = cur.fetchone()
#                        #checks to see if the ID entered already exists. If it does, it will require the user to re enter their ID.
#                        while checkEmpID:
#                            EmpID = input("That EmployeeID is already in use. Please enter a different EmployeeID: ")
#                            stripEmpID = EmpID.strip()
#                            cur.execute("SELECT EmployeeID FROM Employee WHERE(EmployeeID = '" + stripEmpID + "')")
#                            checkEmpID = cur.fetchone()
#                        print("EmployeeID, " + stripEmpID + ", is accepted")
#                        
#                        #List of requirements below and some constraints listed for them.
#                        firstName     = input("\nWhat is your first name? ")
#                        if firstName and firstName.isalpha():
#                            pass
#                        elif firstName and firstName.isdigit():
#                            print ("Name must be Alphabet characters only!")
#        
#                        lastName      = input("What is your last name? ")
#                        if lastName and lastName.isalpha():
#                            pass
#                        elif lastName and lastName.isdigit():
#                            print ("Last name must be Alphabet characters only!")
#                        
#                        streetAddress = input("What is your street address? ")
#                        
#                        city          = input("What city do you live in? ")
#                        if city and city.isalpha():
#                            pass
#                        elif city and city.isdigit():
#                            print ("City must be Alphabet characters only!")
#                        
#                        state         = input("What state do you live in? ")
#                        if state and state.isalpha():
#                            pass
#                        elif state and state.isdigit():
#                            print ("State must be Alphabet characters only!")
#                        
#                        zipCode       = input("What is your zipcode? ")
#                        
#                        email         = input("What is your email? ")
#                        
#                        while "@" not in email:
#                            email = input("Invalid email address, please try again: ")
#                                
#                        password      = input("What is your password? ")                    
#        
#                        cur.execute('''INSERT INTO Employee VALUES(?,?,?,?,?,?,?,?,?)''', (stripEmpID, firstName, lastName, streetAddress, city, state, zipCode, email, password))
#                        conn.commit()
#        
#                    except:
#                        print("Connection Failed")
#        except:
#            print("Connection Failed")
#            
#def menuOptions():
#    
#    print("========= WELCOME TO THE WINE REPOSITORY =========")
#    print("\nA) Login")
#    print("B) Not a member? Register Here.")
#    print("C) Exit the program")
#    print("\n==================================================")
#
#    menu_option = input("Please select an option to continue: ")
#    menu_option = menu_option.lower()
#
#    if menu_option == "a":
#        login()
#    elif menu_option == "b":
#        register()
#    elif menu_option == "c":
#        exit()
#
#if __name__ == "__main__":
#    online = False
#    while not online:
#        menuOptions()
#    if online:
#        print("CHECKPOINT")
        

#import pandas as pd
#
#allWines = pd.read_csv('winequality-both.csv', sep=',' , header=0 )
#
#red = allWines.loc[allWines['type']== "red", :]
#white = allWines.loc[allWines['type']== "white", :]
#
#
#import pandas as pd
#import scipy.stats
#try:
#    
#    WineCharX = "quality"
#    WineCharY = "volatike acidity"
#    allWines = pd.read_csv('winequality-both.csv')
#    red = allWines.loc[allWines['type']=='red', :]
#    white = allWines.loc[allWines['type']=='white', :]
#    
#    getCorr = scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
#    correlation = str(getCorr[0])
#    pValue = str(getCorr[1])
#    print("For red wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
#    print("With p value of: " + pValue)
#    
#    CorrMessage = "Here are the correlation and p value for " + WineCharX +"and " + WineCharY
#    print(CorrMessage + " for white wine: ")
#    print(scipy.stats.pearsonr(white[WineCharX], white[WineCharY]))
#    
#    
#except (KeyError) as e:
#    print ('Please check the spelling of the wine charactersistics you want to test')
#    
    
#import seaborn
#import matplotlib.pyplot as plt
#import pandas as pd
#import scipy.stats
#
#from pylab import savefig
#try:
#    WineCharX = "quality"
#    WineCharY = "volatile acidity"
#    allWines = pd.read_csv('winequality-both.csv')
#    white = allWines.loc[allWines['type']=='white', :]
#    getCorr =scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
#    correlation = str(getCorr[0])
#    pValue = str(getCorr[1])
#    print("For white wine, the correlationbetween " + WineCharX + " and " + WineCharY + " is " + correlation)
#    print("With p value of: " + pValue)
#    
#    seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
#    plt.xlabel(WineCharX)
#    plt.ylabel(WineCharY)
#    plt.title("White Wine: "+ WineCharX + " X " + WineCharY)
#    savefig("scatterplit1.png")
#except (KeyError) as e:
#    print ('Please check the spelling of the wine characteristics you want to test')    
#    
#
#
#from pylab import savefig
#try:
#    WineCharX = "quality"
#    WineCharY = "volatile acidity"
#    allWines = pd.read_csv('winequality-both.csv')
#    red = allWines.loc[allWines['type']=='red', :]
#    getCorr =scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
#    correlation = str(getCorr[0])
#    pValue = str(getCorr[1])
#    print("For red wine, the correlationbetween " + WineCharX + " and " + WineCharY + " is " + correlation)
#    print("With p value of: " + pValue)
#    
#    seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
#    plt.xlabel(WineCharX)
#    plt.ylabel(WineCharY)
#    plt.title("Red Wine: "+ WineCharX + " X " + WineCharY)
#    savefig("scatterplit1.png")
#except (KeyError) as e:
#    print ('Please check the spelling of the wine characteristics you want to test')
#    
#from pylab import savefig
#try:
#    WineCharX = "quality"
#    WineCharY = "fixed acidity"
#    allWines = pd.read_csv('winequality-both.csv')
#    red = allWines.loc[allWines['type']=='red', :]
#    getCorr =scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
#    correlation = str(getCorr[0])
#    pValue = str(getCorr[1])
#    print("For red wine, the correlationbetween " + WineCharX + " and " + WineCharY + " is " + correlation)
#    print("With p value of: " + pValue)
#    
#    seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
#    plt.xlabel(WineCharX)
#    plt.ylabel(WineCharY)
#    plt.title("Red Wine: "+ WineCharX + " X " + WineCharY)
#    savefig("scatterplit1.png")
#except (KeyError) as e:
#    print ('Please check the spelling of the wine characteristics you want to test')   
#    
#
#from pylab import savefig
#try:
#    WineCharX = "quality"
#    WineCharY = "fixed acidity"
#    allWines = pd.read_csv('winequality-both.csv')
#    white = allWines.loc[allWines['type']=='white', :]
#    getCorr =scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
#    correlation = str(getCorr[0])
#    pValue = str(getCorr[1])
#    print("For white wine, the correlationbetween " + WineCharX + " and " + WineCharY + " is " + correlation)
#    print("With p value of: " + pValue)
#    
#    seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
#    plt.xlabel(WineCharX)
#    plt.ylabel(WineCharY)
#    plt.title("white Wine: "+ WineCharX + " X " + WineCharY)
#    savefig("scatterplit1.png")
#except (KeyError) as e:
#    print ('Please check the spelling of the wine characteristics you want to test')   


import seaborn
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
from pylab import savefig

allWines = pd.read_csv('winequality-both.csv', sep=',',header=0)
red = allWines.loc[allWines['type']=='red', :]
white = allWines.loc[allWines['type']=='white', :]

#test the volatile acidity and wine quality
def option_1():
    try:
        WineCharX = "quality"
        WineCharY = "volatile acidity"
        allWines = pd.read_csv('winequality-both.csv')
        white = allWines.loc[allWines['type']=='white', :]
        getCorr =scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("White Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')
    
def option_2():
    try:
        WineCharX = "quality"
        WineCharY = "volatile acidity"
        allWines = pd.read_csv('winequality-both.csv')
        red = allWines.loc[allWines['type']=='red', :]
        getCorr =scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("Red Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')

#test the fixed acidity and wine quality
def option_3():

    try:
        WineCharX = "quality"
        WineCharY = "fixed acidity"
        allWines = pd.read_csv('winequality-both.csv')
        white = allWines.loc[allWines['type']=='white', :]
        getCorr =scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("White Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')

def option_4():   
    
    try:
        WineCharX = "quality"
        WineCharY = "fixed acidity"
        allWines = pd.read_csv('winequality-both.csv')
        red = allWines.loc[allWines['type']=='red', :]
        getCorr =scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("Red Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')
        
#test the alcohol percent and wine quality
def option_5():
   
    try:
        WineCharX = "quality"
        WineCharY = "alcohol"
        allWines = pd.read_csv('winequality-both.csv')
        white = allWines.loc[allWines['type']=='white', :]
        getCorr =scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("White Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')

def option_6():        
    
    try:
        WineCharX = "quality"
        WineCharY = "alcohol"
        allWines = pd.read_csv('winequality-both.csv')
        red = allWines.loc[allWines['type']=='red', :]
        getCorr =scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("\nFor red wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("Red Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')
        
#test the residual sugar and wine quality 
def option_7():
    
    try:
        WineCharX = "quality"
        WineCharY = "residual sugar"
        allWines = pd.read_csv('winequality-both.csv')
        white = allWines.loc[allWines['type']=='white', :]
        getCorr =scipy.stats.pearsonr(white[WineCharX], white[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("\nFor white wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=white)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("White Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')

def option_8():        
    
    try:
        WineCharX = "quality"
        WineCharY = "residual sugar"
        allWines = pd.read_csv('winequality-both.csv')
        red = allWines.loc[allWines['type']=='red', :]
        getCorr =scipy.stats.pearsonr(red[WineCharX], red[WineCharY])
        correlation = str(getCorr[0])
        pValue = str(getCorr[1])
        print("For red wine, the correlation between " + WineCharX + " and " + WineCharY + " is " + correlation)
        print("With p value of: " + pValue)
        
        seaborn.lmplot(x=WineCharX, y=WineCharY, data=red)
        plt.xlabel(WineCharX)
        plt.ylabel(WineCharY)
        plt.title("Red Wine: "+ WineCharX + " X " + WineCharY)
        savefig("scatterplit1.png")
    except (KeyError) as e:
        print ('Please check the spelling of the wine characteristics you want to test')

    

 
def menuOptions():
     print("\n \nA) Test Volitile acidity and Wine Quality for White Wine")
     print("\n \nB) Test Volitile acidity and Wine Quality for Red Wine")
     print("\n \nC) Test Fixed Acidity and Wine Quality for Withe Wine")
     print("\n \nD) Test Fixed Acidity and Wine Quality for Red Wine")
     print("\n \nE) Test Alcohol and Wine Quality for White Wine")
     print("\n \nF) Test Alcohol and Wine Quality for Red Wine")
     print("\n \nG) Test Residual Sugar and Wine Quality for White Wine")
     print("\n \nH) Test Residual Sugar and Wine Quality for Red Wine")
 
     menu_option = input("\n Please select an option to continue: ")
     menu_option = menu_option.lower()
 
     if menu_option == "a":
         option_1()
     elif menu_option == "b":
         option_2()
     elif menu_option == "c":
         option_3()
     elif menu_option == "d":
         option_4()
     elif menu_option == "e":
         option_5()
     elif menu_option == "f":
         option_6()
     elif menu_option == "g":
         option_7()
     elif menu_option == "h":
         option_8()
     elif menu_option != "" :
         "not valid choice, try again" ()
         

if __name__ == "__main__":
     online = False
     while not online:
         menuOptions()
     if online:
         print("CHECKPOINT")  

    
    

    
    
