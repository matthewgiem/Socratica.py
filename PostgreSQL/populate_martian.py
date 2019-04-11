import psycopg2
password = open('database_password.txt', 'r').read()

def create_and_populate_martian_tables():
    commands = [
    # create base table
        """
        CREATE TABLE base
        (
            base_id SERIAL PRIMARY KEY,
            base_name character varying,
            founded date
        )
        ;""",
    # create martian table
        """
        CREATE TABLE martian
        (
            martian_id SERIAL PRIMARY KEY,
            first_name character varying,
            last_name character varying,
            base_id integer,
            super_id integer,
            FOREIGN KEY (base_id)
            REFERENCES base (base_id)
        );""",
    # populate base table
        """
        INSERT INTO
            base (base_id, base_name, founded)
        VALUES
            (1, 'Tharsisland', '2037-06-03'),
            (2, 'Valles Marineris 2.0', '2040-12-01'),
            (3, 'Gale Cratertown', '2041-08-15'),
            (4, 'New New New York', '2042-02-10'),
            (5, 'Olympus Mons Spa & Casino', NULL)
        ;""",
    # populate martian table
        """
        INSERT INTO
            martian (martian_id, first_name, last_name, base_id, super_id)
        VALUES
            (1, 'Ray', 'Bradbury', 1, NULL),
            (2, 'John', 'Black', 4, 10),
            (3, 'Samuel', 'Hinkston', 4, 2),
            (4, 'Jeff', 'Spender', 1, 9),
            (5, 'Sam', 'Parkhill', 2, 12),
            (6, 'Elma', 'Parkhill', 3, 8),
            (7, 'Melissa', 'Lewis', 1, 1),
            (8, 'Mark', 'Watney', 3, NULL),
            (9, 'Beth', 'Johanssen', 1, 1),
            (10, 'Chris', 'Beck', 4, NULL),
            (11, 'Nathaniel', 'York', 4, 2),
            (12, 'Elon','Musk' , 2, NULL),
            (13, 'John', 'Carter', NULL, 8)
        ;"""
    ]
    conn = None
    try:
        conn = psycopg2.connect('dbname=martian user=postgres password={}'.format(password))
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# if __name__ == '__main__':
#     create_and_populate_martian_tables()
