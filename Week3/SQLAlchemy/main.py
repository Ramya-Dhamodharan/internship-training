#Here we perform all the CRUD operations
from database import engine, SessionLocal, Base
from models import User, Post

Base.metadata.create_all(bind=engine)
print("Tables created!")

session = SessionLocal()

user1 = User(name="Ramya", email="ramya@example.com", age=22)
user2 = User(name="Priya", email="priya@example.com", age=24)
user3 = User(name="Ravi",  email="ravi@example.com",  age=21)

session.add(user1)
session.add(user2)
session.add(user3)
session.commit() 

print("users added successfully")

post1 = Post(title="Python Basics",   content="All about Python",  user_id=user1.id)
post2 = Post(title="FastAPI Guide",   content="Building APIs",     user_id=user1.id)
post3 = Post(title="SQL Joins",       content="Inner vs Left",     user_id=user2.id)
post4 = Post(title="ORM vs Raw SQL",  content="When to use each",  user_id=user1.id)

session.add_all([post1, post2, post3, post4])
session.commit()

print("posts added succesfully")

#select 
all_users = session.query(User).all()
for user in all_users:
    print(user)

older_users = session.query(User).filter(User.age > 21).all()
for user in older_users:
    print(user)

sorted_users = session.query(User).order_by(User.age.desc()).all()
for user in sorted_users:
    print(f"{user.name} — age {user.age}")

