
from call_api import read_api, mysql_config
from datetime import datetime

# getting data from call_api
def get_data():
    articles = read_api()
    mysql_dict = mysql_config()
    connection = mysql_dict['connection']
    cursor = mysql_dict['cursor']
    return {'articles':articles, 'connection':connection, 'cursor':cursor}

 # function is responsiable for create a table and load data into table
def table_operation():
    #   CREATING TABLE IF IT NOT EXISTS
    create_table ="""
    CREATE TABLE IF NOT EXISTS articles(
        source_id TEXT,
        source_name TEXT,
        author TEXT,
        title TEXT,
        description TEXT,
        url TEXT,
        urltoimage TEXT,
        publishedat TEXT,
        content TEXT
        )"""
    cursor.execute(create_table)

    
    #inserting data into table
    for article in articles:

        insert_column = """INSERT INTO articles 
        (source_id, source_name,
        author, title, 
        description, url, 
        urltoimage, publishedat, 
        content)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # valuse 
        data_to_insert =(article['source']['id'], article['source']['name'],article['author'], article['title'], article['description'], article['url'], article['urlToImage'],article['publishedAt'],article['content'] )

        #storing values in table 
        cursor.execute(insert_column, data_to_insert)
    connection.commit()
    connection.close()
    print('Data inserted successfully', datetime.now())


#getting data through get_data function
get_dict = get_data()
articles = get_dict['articles']
connection = get_dict['connection']
cursor = get_dict['cursor']

# adding data into table

add = table_operation()
