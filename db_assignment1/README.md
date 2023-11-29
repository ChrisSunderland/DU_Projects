# **DB Organization & Mgmt- Assignment 1**

## **Description**

This folder contains an assignment I completed as part of a database organization & management course. The objective of the assignment was to develop several Python scripts that queried a MySQL relational database for the fictional ‘Henry’ bookstore chain. If one wrote the correct SQL commands and performed the necessary joins, one could then use a Tkinter GUI to search for books by author name, genre, or publisher name. Successful searches displayed the price of a book as well as the store location where one could purchase a title of interest.

## **Usage / Requirements**


To recreate this assignment, the SQL commands within the ‘Henry_setup.sql’ file first have to be executed. This file was provided by the course instructor and creates / fills a series of tables that contain the names of authors, book titles, etc.

After this is done, running the ‘Henry.py’ file will display a GUI from which one is then able to search for a title. The ‘Henry.py’ file is able to do this because it imports a class from ‘henryDAO.py’ that's comprised of methods that query the tables within the database.

The following packages are also needed:

* mysql-connector-python 8.0.31
* python-dotenv 1.0.0
* tkinter 0.3.1
