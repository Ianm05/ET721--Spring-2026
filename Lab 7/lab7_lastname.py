"""
import sys
print(sys.executable)

Ian Martinez
Feb 19, 2026
lab 7 working with data in python
"""

print("\n---- Example 1: read file")
with open("Phrases.txt", "r") as file1:
    filecontent1 = file1.readline(30)
    filecontent2 = file1.readline(5)

    print(filecontent1)
    print(filecontent2)

    print(f"\nIs the file closed? {file1.closed}")

print("\n---- Example 2: readline file")
with open("Phrases.txt", "r") as file1:
    filecontent = file1.readlines(30)
    print(filecontent)

print("\n ---- Example 3: readlines file")
with open("Phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    print(filecontent)

print("\n ---- Example 4: loop through each line in the file")
with open("Phrases.txt", "r") as file1:
    for eachline in file1:
        print(eachline.strip())

print("\n ----- Example 5: create file")
with open("lastname.txt", "w") as file:
    file.write("Python basics for data science\n")
    file.write("Ian Martinez")

print("\n------ Example 6: append data into an existing file")
from datetime import datetime

with open("lastname.txt", "a") as file:
    file.write(f"\nLast update: {datetime.now()}")

print("\n------ Example 7: copy a file")
with open("lastname.txt", "r") as readfile:
    with open("newfile.txt", "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)

print("\n------ Example 8: pandas a file")
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

df = pd.DataFrame(data)
print(df)

print("\n------ Example 9: creating df with pandas from an excel file")
try:
    df_excel = pd.read_excel("classdata.xlsx")
    print(df_excel)
    print(df_excel.head())
except FileNotFoundError:
    print("classdata.xlsx not found in folder")

# 
print("\n------ Exercise 1:")

def email_read():
    gmail = 0
    yahoo = 0
    hotmail = 0

    try:
        with open("user_email.txt", "r") as infile:
            for line in infile:
                email = line.strip().lower()

                if "@gmail" in email:
                    gmail += 1
                elif "@yahoo" in email:
                    yahoo += 1
                elif "@hotmail" in email:
                    hotmail += 1

        with open("reportemail.txt", "w") as outfile:
            outfile.write(f"gmail = {gmail}\n")
            outfile.write(f"yahoo = {yahoo}\n")
            outfile.write(f"hotmail = {hotmail}\n")

        return gmail, yahoo, hotmail
    
    except FileNotFoundError:
        print("Error: user_email.txt file not found.")
        return (0, 0, 0)
    
result = email_read()

if result:
    print("Report created successfully!")

result = email_read()
print(result)