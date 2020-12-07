'''
-------------------
Name: problem1.py

Purpose: Caculates degrees in fahrenheit from celsius

Author: Daniel Monzer

Created: 07/12/20
-------------------
'''
#Display what this program is used for
print("***Celsius to fahrenheit Converter***")
#Create the input for the user to type their answer
celsius = float(input("Type the temperature in celsius: "))
#Calculate the degrees in fahrenheit
fahrenheit = (9/5 * celsius) + 32
#Print the degrees in fahrenheit
print("The temperature is",fahrenheit,"degrees fahrenheit")