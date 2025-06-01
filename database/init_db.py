import psycopg2
from psycopg2 import sql

def run_sql_file(filename, conn):
    with open(filename, 'r') as file:
        sql_commands = file.read()
    with conn.cursor() as cur:
        cur.execute(sql_commands)
    conn.commit()

def main():
    # Update with your DB credentials
    conn_params = {
        'dbname': 'student_course_db',
        'user': 'postgres',
        'password': 'zx0cv0bn0m',
        'host': 'localhost',
        'port': 5432
    }

    try:
        conn = psycopg2.connect(**conn_params)
        print("Connected to database")

        print("Creating schema...")
        run_sql_file('database/schema.sql', conn)

        print("Inserting sample data...")
        run_sql_file('database/sample_data.sql', conn)

        print("Database initialized successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
