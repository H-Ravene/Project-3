#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#In this jupyter notebook we will be creating a pandas DataFrame that displays Customers’ Last Name and First Name, and each customer’s purchased Track names and Album Titles
#Importing  mysql.connector library
import mysql.connector as sql
#Importing the pandas library
import pandas as pd
#Connecting to the Chinook database 
sql_connection = sql.connect(host='127.1.0.1', database='chinook', user='herve', password='project3')

#Saving the SQL query to execute
sql_query = ("SELECT                 customer.LastName AS 'First_Name',                 customer.FirstName AS 'Last_Name',                 track.Name AS 'Song_Title',                 album.Title AS 'Album_Title'                 FROM customer                 JOIN invoice                     ON customer.CustomerId = invoice.CustomerId                 JOIN invoiceline                     ON invoice.InvoiceId = invoiceline.InvoiceId                 JOIN track                     ON invoiceline.TrackId = track.TrackId                 JOIN Album                     ON track.AlbumId = Album.AlbumId                 ORDER BY customer.LastName, album.Title ASC, track.name ASC")
#Reading the SQL query into a pandas dataframe
purchased_songs = pd.read_sql(sql_query, sql_connection)
#Displaying the information
purchased_songs

