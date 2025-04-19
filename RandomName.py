#python
import random
import string
import names


def generate_random_name():
   random_names = [names.get_full_name() for _ in range(10000)]

   #return ''.join(random.choices(string.ascii_letters, k=8))
   first_names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Jamie', 'Riley', 'Skyler', 'Avery', 'Peyton']
   last_names = ['Smith', 'Johnson', 'Lee', 'Brown', 'Garcia', 'Martinez', 'Davis', 'Clark', 'Lewis', 'Walker']
   return f"{random.choice(first_names)} {random.choice(last_names)}"
def generate_random_id():
   return ''.join(random.choices(string.digits, k=5))
def generate_random_grade():
   return random.uniform(0., 100)
def generate_random_attendance():
   return random.randint(0, 100)
data = []
for _ in range(10000):
   name = generate_random_name()
   id = generate_random_id()
   grade = generate_random_grade()
   attendance = generate_random_attendance()
   data.append({'Name': name, 'ID': id, 'Grade': grade, 'Attendance%': attendance})
# Print the first 10 entries to verify
for entry in data[:20]:
   print(entry)