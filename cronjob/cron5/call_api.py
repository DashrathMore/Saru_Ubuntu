import mysql.connector
import requests
import yaml



def open_yml():

    # opening env.yml file and getting data 
    with open('/usr/src/app/env.yml','r') as fo:
        conf = yaml.safe_load(fo)
    return conf

# def read data 
def read_api():
    conf = open_yml()
    # getting key from env.yml
    key = conf.get('api_key')
    # getting Current date from env.yml
    date = conf.get('date')

    url = f'https://newsapi.org/v2/everything?q=tesla&from={date}&sortBy=publishedAt&apiKey={key}'
    response = requests.get(url)
    data_api = response.json()
    articles = data_api.get('articles',[])
    return articles


# Making connection with mysql
def mysql_config():
    conf = open_yml()

    # Getting MMYSQL conf from env.yml
    mysql_conf = {
        'host' : conf.get('mysql_host'),
        'user' : conf.get('mysql_user'),
        'password' : conf.get('mysql_password'),
        'database' : conf.get('mysql_database')
    }
    
    connection = mysql.connector.connect(**mysql_conf)

    # Getting connection and cursor
    return {'connection':connection, 'cursor' : connection.cursor()}

