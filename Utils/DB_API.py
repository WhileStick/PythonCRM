from mysql.connector import connect, Error

from Config import *


class DB:

    def __init__(self):
        self.create_tables()
        try:
            print("Trying to connect to database...")
            with connect(
                    host=DB_HOST,
                    user=DB_USER,
                    password=DB_PASS,
                    database=DB_NAME) as connection:
                print("Connection Successful")
        except Error as e:
            print("Connection failed: database doesn't exist")
            self.create_database()
            self.create_tables()

    def create_database(self):
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS) as server_conn:
            print("Connecting to MySQL server...")
            query = f"CREATE DATABASE {DB_NAME}"
            with server_conn.cursor() as cursor:
                print(f"Creating database {DB_NAME}...")
                cursor.execute(query)
                print(f"Database {DB_NAME} created successfully")

    def create_tables(self):
        print("Creating tables...")
        with connect(host=DB_HOST, user=DB_USER, password=DB_PASS,
                     database=DB_NAME) as connection:
            with connection.cursor() as cursor:
                users = """CREATE TABLE IF NOT EXISTS users(
                id INT AUTO_INCREMENT PRIMARY KEY,
                login VARCHAR(255),
                password VARCHAR(255)
                );"""

                partners = """CREATE TABLE IF NOT EXISTS partners(
                pid INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) UNIQUE,
                finances VARCHAR(255),
                contacts VARCHAR(255),
                access VARCHAR(255),
                brand VARCHAR(255),
                percent FLOAT,
                deposit FLOAT);
                """

                clients = """CREATE TABLE IF NOT EXISTS clients(
                id INT AUTO_INCREMENT PRIMARY KEY,
                flight_date DATE NOT NULL,
                flight VARCHAR(255),
                country VARCHAR(255),
                status VARCHAR(255),
                visa VARCHAR(255),
                operator VARCHAR(255),
                return_date DATE NOT NULL,
                partner INT,
                FOREIGN KEY (partner) REFERENCES partners(pid),
                bron VARCHAR(255),
                customer VARCHAR(255),
                deposit FLOAT,
                profit FLOAT);                
                """
                for elem in [users, partners, clients]:
                    cursor.execute(elem)
                connection.commit()
                print("Table 'users' created!")

    def execute(self, query, *args, fetchone=False, fetchall=False, insert=False):
        with connect(host=DB_HOST, user=DB_USER, password=DB_PASS,
                     database=DB_NAME) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, *args)
                if fetchall:
                    return cursor.fetchall()
                elif fetchone:
                    return cursor.fetchone()
                elif insert:
                    connection.commit()

    def get_user(self, login):
        # <=> используется для безопасного сравнения с NULL-значениями ("< = >" но без пробелов)
        query = "SELECT * FROM users WHERE login <=> (%s);"
        res = self.execute(query, (login,), fetchone=True)
        return res

    def has_user(self, login):
        res = self.get_user(login)
        return res is not None

    def try_to_auth(self, login, password):
        if self.has_user(login):
            user_line = self.get_user(login)
            return user_line[2] == password
        return False

    def get_all_users(self):
        query = "SELECT * FROM users;"
        try:
            res = self.execute(query, fetchall=True)
            print("OK")
            print(res)
        except Exception as e:
            print(e)

    def get_all_clients(self):
        try:
            """
            query = "SELECT clients.id, clients.flight_date, clients.flight," \
                    "clients.country, clients.status, clients.visa, clients.operator," \
                    "clients.return_date, partners.name, clients.bron, clients.customer," \
                    "clients.deposit, clients.profit FROM clients LEFT JOIN partners ON" \
                    "clients.partner = partners.pid;"
                    """
            query = "SELECT clients.id, clients.flight_date, clients.flight," \
                    " clients.country, clients.status, clients.visa," \
                    " clients.operator, clients.return_date, partners.name," \
                    " clients.bron, clients.customer," \
                    " clients.deposit, clients.profit" \
                    "  FROM clients LEFT JOIN partners " \
                    "ON clients.partner = partners.pid;"
            res = self.execute(query, fetchall=True)
            return res
        except Exception as e:
            print(e)

    def get_all_partners(self):
        query = "SELECT * FROM partners;"
        res = self.execute(query, fetchall=True)
        return res

    def get_new_client_id(self):
        query = "SELECT MAX(id) FROM clients;"
        res = self.execute(query, fetchone=True)
        return res if res[0] is not None else 0
    
    def add_partner(self, values):
        query = "INSERT INTO partners(name, finances, contacts, access, brand, percent, deposit)" \
                " VALUES(%s, %s, %s, %s, %s, %s, %s);"
        res = self.execute(query, values, insert=True)
        return res

    def get_partners_options(self):
        query = "SELECT pid, name FROM partners;"
        res = self.execute(query, fetchall=True)
        return res

    def add_client(self, values):
        query = "INSERT INTO clients(flight_date, flight, country," \
                "status, visa, operator, return_date, partner, bron," \
                "customer, deposit, profit) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        res = self.execute(query, values, insert=True)
        return res

    def get_flights_on(self, month, year):
        query1 = "SELECT id, flight_date FROM clients" \
                " WHERE YEAR(flight_date) = %s AND" \
                " MONTH(flight_date) = %s"
        flights = self.execute(query1, [year, month], fetchall=True)

        query2 = "SELECT id, return_date FROM clients" \
                " WHERE YEAR(return_date) = %s AND" \
                " MONTH(return_date) = %s"
        returns = self.execute(query1, [year, month], fetchall=True)
        return [flights, returns]


