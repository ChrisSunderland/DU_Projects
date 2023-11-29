# **Data Migration Assignment**

With the help of a classmate, this was another assignment I completed as part
of the database organization & management course I took at DU. Given a large
dataset containing video game sales data (vgsales.csv), students in the class were
asked to normalize the data and use its fields to design a MySQL relational
database. We then had to migrate the contents of the file into the database we designed.
Lastly, my partner and I developed a series of stored procedures that performed
common queries on the database. The work to do all of this can be found in the
following files:

* vgMigration.sql
* vgStoredProcedures.sql
* vgCalls.sql

In this folder, one can also find a Crow's Foot Diagram that breaks down the
relationships between the tables we ultimately created. Additionally, there's a brief
writeup explaining the rationale behind the design of our database.

## **Data Dictionary**

Fields from the original 'vgsales.csv' file:

| Attribute | Description |
|----------|----------|
| Name | video game title |
| Platform | video game console |
| Year | sales year of interest |
| Genre | video game genre |
| Publisher | video game publisher |
| NA_Sales | amount sold in North America |
| EU_Sales | amount sold in Europe |
| JP_Sales | amount sold in Japan |
| Other_Sales | amount sold ROW |
| Global_Sales | total amount sold worldwide |

## **Usage**

To set up this database on your own machine, you'll first need to install the
mysql-connector-python library (version 8.0.31). You'll then need to run the
'loadVG.py' script. Doing this will move the data from the original csv into
a MySQL table. Executing the commands within 'vgMigration.sql' will then take
this raw data and migrate it into the tables of the relational database that
we designed.
