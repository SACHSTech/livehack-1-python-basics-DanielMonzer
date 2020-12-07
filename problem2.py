'''
-------------------
Name: problem2.py

Purpose: Calculates number of chickens split between the students and Mr.Fabroa

Author: Daniel Monzer

Created: 07/12/20
-------------------
'''
#Create an input for the user to type the amount of students
students = int(input("How many students are in the class?: "))
#Create an input for the user to type the amount of chicken
chicken = int(input("How many pieces of chicken are there?: "))
#Print how much chicken each student will get
print("Each student will get",chicken // students,"pieces of chicken")
#Print how much chicken will Mr.Fabroa get
print("Mr. Fabroa will get",chicken % students,"pieces of chicken")