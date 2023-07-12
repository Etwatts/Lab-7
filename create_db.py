"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime
import random
# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""

    # Establishes a connection to the database
    con = sqlite3.connect(db_path)

    # Gets cursor object that can be used to run SQL queries on the database
    cur = con.cursor()

    # Creates spreadsheet to add data
    create_table_query = """
    CREATE TABLE IF NOT EXISTS people
    (
        id INTIGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        province TEXT NOT NULL,
        bio TEXT,
        age INTEGER,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL
    );
    """
    cur.execute(create_table_query)

    con.commit()

    con.close()
    
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Generate fake data using faker
    fake = Faker("en_CA")

    # Generate fake data for 200 fake people 
    for i in range(200):
      name = fake.name()
      email = fake.email()
      address = fake.address().replace("\n", ", ")
      city = fake.city()
      province = fake.province()
      bio = fake.paragraph()
      age = fake.random_int(min=1, max=100)
      created_at = datetime.now()
      updated_at = datetime.now()

      insert_person_query = """
      INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
      """
      cur.execute(insert_person_query, (name, email, address, city, province, bio, age, created_at, updated_at))

    con.commit()
    con.close()
        
    return

if __name__ == '__main__':
   main()