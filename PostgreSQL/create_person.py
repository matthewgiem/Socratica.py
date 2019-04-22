import psycopg2
password = open('database_password.txt', 'r').read()

def create_persons():
    command = [
    # CREATE TABLE for person
    """
    CREATE TABLE persons
    (
        person_id SERIAL PRIMARY KEY,
        first_name character varying,
        last_name character varying,
        birthday timestamp without time zone
    );"""]
    conn = None
    try:
        conn = psycopg2.connect('dbname=person user=postgres password={}'.format(password))
        cur = conn.cursor()
        for command in command:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    create_persons()
