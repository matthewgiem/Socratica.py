import psycopg2
password = open('database_password.txt', 'r').read()

def create_and_populate_martian_tables():
    commands = [
    create base table
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
    create visitor table
        """
        CREATE TABLE visitor
        (
            visitor_id SERIAL PRIMARY KEY,
            host_id integer,
            first_name character varying,
            last_name character varying,
            FOREIGN KEY (host_id)
            REFERENCES martian (martian_id)
        )
        ;""",
    # create supply table
    """
    CREATE TABLE supply
    (
        supply_id SERIAL PRIMARY KEY,
        name character varying,
        description character varying,
        quantity integer
    )
    ;""",
    # create inventory table
    """
    CREATE TABLE inventory
    (
        base_id integer,
        supply_id integer,
        quantity integer,
        FOREIGN KEY (base_id)
        REFERENCES base (base_id),
        FOREIGN KEY (supply_id)
        REFERENCES supply (supply_id)
    )
    ;""",
    create martian_confidential
    """
    CREATE TABLE martian_confidential
    (
        martian_id SERIAL PRIMARY KEY,
        first_name character varying,
        last_name character varying,
        base_id integer,
        super_id integer,
        salary integer,
        dna_id character varying,
        FOREIGN KEY (base_id)
        REFERENCES base (base_id)
    )
    ;""",
    # # populate supply table
    """
    INSERT INTO
        supply (supply_id, name, description, quantity)
    VALUES
        (1, 'Solar Panel', 'Standard 1X1 meter cell', 912),
        (2, 'Water Filter', $$This takes things out of your water so it's drinkable$$, 6),
        (3, 'Duct Tape', 'A 10 meter roll of duct tape for ALL your repairs.', 951),
        (4, 'Ketchup', $$It's ketchup...$$, 206),
        (5, 'Battery Cell', 'Standard 1000 kAh battery cell for power grid (heavy item).', 17),
        (6, 'USB 6.0 Cable', 'Carbon fiber coated / 15 TBps spool', 42),
        (7, 'Fuzzy Duster', 'It gets dusty around here. Be prepared!', 19),
        (8, 'Mars Bars', 'The ORIGINAL nutrient bar made with the finest dioengineered ingredients.', 3801),
        (9, 'Air Filter', 'Removes 99% of all Martian dust from your ventilation unit', 23),
        (10, $$Famous Ray's Frozen Pizza$$, 'this Martian favorite is covered in all your favorite toppings. 1 flavor only.', 823)
    ;""",
    # populate inventory table
    """
    INSERT INTO
        inventory (base_id, supply_id, quantity)
    VALUES
        (1, 1, 8),
        (1, 3, 5),
        (1, 5, 1),
        (1, 6, 2),
        (1, 8, 12),
        (1, 9, 1),
        (2, 4, 5),
        (2, 8, 62),
        (2, 10, 37),
        (3, 2, 11),
        (3, 7, 2),
        (4, 10, 91)
    ;""",
    # populate visitor table
        """
        INSERT INTO
            visitor (visitor_id, host_id, first_name, last_name)
        VALUES
            (1, 7, 'George', 'Ambrose'),
            (2, 1, 'Kris', 'Cardenas'),
            (3, 9, 'Priscilla', 'Lane'),
            (4, 11, 'Jane', 'Thornton'),
            (5, NULL, 'Doug', 'Stavenger'),
            (6, NULL, 'Jamie', 'Waterman'),
            (7, 8, 'Martin', 'Humphries')
        ;""",
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
        ;""",
        populate martian_confidential
        """
        INSERT INTO
            martian_confidential (martian_id, first_name, last_name, base_id, super_id, salary, dna_id)
        VALUES
        (1, 'Ray', 'Bradbury', 1, NULL, 155900, 'gctaggaatagaatctcctgttg'),
        (2, 'John', 'Black', 4, 10, 120100, 'cagttaatggttgaagctggggatt'),
        (3, 'Samuel', 'Hinkston', 4, 2, 110000, 'cgaagcgctagatgctgtgttgtag'),
        (4, 'Jeff', 'Spender', 1, 9, 10000, 'gactaatgtcttcgtggattgcaga'),
        (5, 'Sam', 'Parkhill', 2, 12, 125000, 'gttactttgcgaaagccgtggctac'),
        (6, 'Elma', 'Parkhill', 3, 8, 137000, 'gcaggatggaagcaactgccatat'),
        (7, 'Melissa', 'Lewis', 1, 1, 145250, 'cttcgatcgtcaatggagtccggac'),
        (8, 'Mark', 'Watney', 3, NULL, 121100, 'gacacgaggcgaactatgtcgcggc'),
        (9, 'Beth', 'Johanssen', 1, 1, 130000, 'cttagactaggtgtgaaacccgtta'),
        (10, 'Chris', 'Beck', 4, NULL, 125000, 'gggggggttacgacgaggaatccat'),
        (11, 'Nathaniel', 'York', 4, 2, 105000, 'ggctccctgggcgggatattggatg'),
        (12, 'Elon', 'Musk', 2, NULL, 155800, 'atctgcttggatcaatagcgctgcg'),
        (13, 'John', 'Carter', NULL, 8, 1295000, 'ccaatcgtgcgagtcgcgatagtct')
        """
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

if __name__ == '__main__':
    create_and_populate_martian_tables()
