from app import app, db, User

with app.app_context():
    db.create_all()
    
    user = User(username='example')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()

    new_greeting = Greeting(message="Welcome to the site!")
    db.session.add(new_greeting)
    db.session.commit()

print("Database and table created successfully!")