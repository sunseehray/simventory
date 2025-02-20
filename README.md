# Overview

As an aspiring software developer, I want to create programs that help with home management. One of the things I struggle with in home management is tracking my food storage. In this program, I attempt to create an inventory app using Python and SQLite 3. By using a SQL relational database, I can do CRUD operations on them and more. 

The Simventory is a simple inventory app that helps users save items to an inventory, view their inventory, update the quantity of an item like adding in or taking from, update the price of an item, and delete an item from the inventory. As a stretch, I also added functionalities to calculate the total value of the inventory on hand and to display the out-of-stock inventory.

[Software Demo Video](http://youtube.com)

# Relational Database

For this project, I am using SQLite which is already supported in Python by importing the sqlite3 library.

The structure of the table has four fields: id, name, quantity, and price with id being the primary key, an INTEGER and auto-incremented. The name is a TEXT that is NOT NULL. The quantity is an INTEGER that is also NOT NULL. Lastly, the price is a REAL number that may be null.

# Development Environment

- VS Code, IDE
- Python 3.10.7
- sqlite3 library
- tabulate

# Useful Websites

- [Python sqlite3](https://docs.python.org/3.8/library/sqlite3.html)
- [SQLite aggregate functions](https://www.sqlitetutorial.net/sqlite-aggregate-functions/)
- [tabulate](https://pypi.org/project/tabulate/)

# Future Work

- Add a date field for expiry dates
- Allow users to view inventory based on expiration date
- Add another table for location of an item such as pantry, freezer, cellar, etc
