import os
import psycopg2
import psycopg2.extras

def connectToDB():
  connectionString = 'dbname=truckcheck user=postgres password=Moore3700 host=localhost'
#   print connectionString
  try:
    return psycopg2.connect(connectionString)
  except:
    print("Can't connect to database")