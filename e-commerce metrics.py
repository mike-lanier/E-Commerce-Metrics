import pandas as pd

Nov = pd.read_csv('2019-Nov.csv', nrows=10000000)


# Creating tables to break down the large dataset

products = Nov[['product_id','category_id','category_code','brand']].drop_duplicates()
products.set_index('product_id', inplace=True)

user_sessions = Nov[['user_session','user_id']].drop_duplicates()
user_sessions.set_index('user_session', inplace=True)

events = Nov[['event_time','event_type','product_id','user_session', 'price']]


events.to_csv('events.csv')
user_sessions.to_csv('sessions.csv')
products.to_csv('products.csv')

