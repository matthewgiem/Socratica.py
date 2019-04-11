import psycopg2
import time

# Number of rows to add in each batch
n = 10000

# Generate single INSERT INTO query
single_query = '''INSERT INTO post (user_id, post_text, posted_on)
    VALUES (1, 'All work and no play makes Jack a dull boy.', current_timestamp);'''

# Generate one BIG query
big_query = 'INSERT INTO post (user_id, post_text, posted_on) VALUES '
for i in range(n):
    big_query += "(1, 'All work and no play makes Jack a dull boy.', current_timestamp),"
big_query = big_query.strip(',') + ';' # Replace trailing ',' with ';'

# Connect to database & create cursor
password = open('database_password.txt', 'r').read()
conn = psycopg2.connect('dbname=Chitter user=postgres password={}'.format(password))
cur = conn.cursor()

# Time the 'n' indicidual queries
start_time = time.time()
for i in range(n):
    cur.execute(single_query)
conn.commit()
stop_time = time.time()
print("it takes {} to make 10,000 queries".format(stop_time-start_time))

start_time = time.time()
cur.execute(big_query)
conn.commit()
stop_time = time.time()
print("while it takes {} to make 1 query with 10,000 entries".format(stop_time-start_time))


# Close both cursor and connection to database
cur.close()
conn.close()
