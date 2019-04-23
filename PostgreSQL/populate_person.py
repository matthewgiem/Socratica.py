import psycopg2
import pandas as pd
import random
import datetime

start = datetime.datetime.now()

password = open('database_password.txt', 'r').read()

last = pd.read_csv('last_names.csv',header=None, usecols=[1])

last_names = last[1].values.tolist()
first_boy = pd.read_csv('male_names.csv',header=None, usecols=[1])
male_first_name = first_boy[1].values.tolist()
first_girl = pd.read_csv('female_names.csv', header=None, usecols=[1])
female_first_name = first_girl[1].values.tolist()
first_names = male_first_name + female_first_name

def populate_person_table():
    conn = None
    try:
        for _ in range(1000):
            conn = psycopg2.connect('dbname=person user=postgres password={}'.format(password))
            cur = conn.cursor()
            commands = []
            for _ in range(100000):
                name = "('{}', '{}', '{}-{}-{}')".format(random.choice(first_names), random.choice(last_names), random.randint(1900,2019), random.randint(1,12), random.randint(1,28))
                commands.append(name)

            command = [
            # populate table
            """
                INSERT INTO
                	persons (first_name, last_name, birthday)
                VALUES
                    {}
            """.format(", ".join(commands))
            ]
            for command in command:
                cur.execute(command)
            cur.close()
            conn.commit()
            end = datetime.datetime.now()
            print(end-start)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    populate_person_table()


end = datetime.datetime.now()
print(end-start)
