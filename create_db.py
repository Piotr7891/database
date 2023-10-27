import psycopg2
from psycopg2 import OperationalError

try:
    conn = psycopg2.connect(host="localhost", dbname="workshop_database", user="postgres", password ="coderslab")
    print("Connection successfull.")
except OperationalError:
    print("Connection failed.")
#USER = "postgres"
#HOST = "localhost"
#PASSWORD = "coderslab"

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    hashed_password VARCHAR(80)
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY ,
    from_id  INTEGER,
    to_id INTEGER,
    creation_date TIMESTAMP,
    text VARCHAR(255),
    FOREIGN KEY (from_id) REFERENCES users(id),
    FOREIGN KEY (to_id) REFERENCES users(id)
);
""")


conn.commit()

cur.close()
conn.close()