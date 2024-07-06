import psycopg2
from faker import Faker
import random

conn = psycopg2.connect(
    dbname='taskmanager',
    user='postgres',
    password='12345',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

fake = Faker()

num_users = 100
num_tasks = 300

for _ in range(num_users):
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fake.name(), fake.unique.email()))

status_names = ['new', 'in progress', 'completed']
for status in status_names:
    cursor.execute("INSERT INTO status (name) VALUES (%s)  ON CONFLICT (name) DO NOTHING", (status,))

cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]

for _ in range(num_tasks):
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (fake.sentence(nb_words=5), fake.text(), random.choice(status_ids), random.choice(user_ids)))

conn.commit()
cursor.close()
conn.close()

print("Completed")