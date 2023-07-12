"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
from create_db import db_path, script_dir
from pprint import pprint
import sqlite3
import csv

def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # querys the sql for anyones name and age over the age of 50
    cur.execute("SELECT name, age FROM people WHERE age >= 50")
    old_list = cur.fetchall()

    con.close()
    
    return old_list

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    # Uses a for loop to print all the names and ages or people in the list
    for name, age in name_and_age_list:
        print(f"{name} is {age} years old.")
    # Hint: Use a for loop to iterate the list of tuples to print a sentence for each old person
    return

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # Creates a csv file to store the names and ages from the list
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows(name_and_age_list)

    # Hint: In Lab 3, we converted a list of tuples into a pandas DataFrame and saved it to a CSV file
    return

if __name__ == '__main__':
   main()