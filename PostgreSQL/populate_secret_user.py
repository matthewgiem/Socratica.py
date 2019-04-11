import psycopg2

query = """
INSERT INTO
    secret_user (first_name, last_name, code_name, country, organization, salary, knows_kung_fu)
VALUES
    ('George' , 'Smiley', 'Beggarman', 'United Kingdom', 'MI6', 97200, false),
    ('Jason', 'Bourne', 'Delta One', 'United States', 'CIA', 115000, false),
    ('Jack' , 'Ryan', NULL, 'United States', 'CIA', 85000, false),
    ('Ethan' , 'Hunt', 'Bravo Echo 1-1', 'United States', 'IMF', 250000, false),
    ('Emma' , 'Peel', 'Mrs. Peel', 'United Kingdom', 'MI6', 972000, true),
    ('Susan' , 'Hilton', 'Agent 99', 'United States', 'Control', 250000, false),
    ('Nick' , 'Fury', 'Foxtrot', 'United States', 'SHIELD', 250000, false)
;"""

password = open('database_password.txt', 'r').read()
conn = psycopg2.connect('dbname=Chitter user=postgres password={}'.format(password))
cur = conn.cursor()

cur.execute(query)
conn.commit()

cur.close()
conn.close()
