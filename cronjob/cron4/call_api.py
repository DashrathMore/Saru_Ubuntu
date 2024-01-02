import mysql.connector
import requests

# def read data 
def read_api():
    #api-key
    key ='3e0b83989687426c9d97d4331b39dd58' 
    #date from which date data we want
    date = '2023-12-07'

    url = f'https://newsapi.org/v2/everything?q=tesla&from={date}&sortBy=publishedAt&apiKey={key}'
    response = requests.get(url)
    data_api = response.json()
    articles = data_api.get('articles',[])
    return articles


# Making connection with mysql
def mysql_config():

    host = 'localhost' 
    user = 'Dashrath'
    password = 'Dashrath'
    database = 'example1'

    
    connection = mysql.connector.connect(host=host, user=user, password=password, database=database)

    # Getting connection and cursor
    return {'connection':connection, 'cursor' : connection.cursor()}
