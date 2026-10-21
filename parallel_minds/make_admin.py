# make_admin.py
from app import create_app
from models import db, User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    hashed_password = generate_password_hash("admin123", method='pbkdf2:sha256')
    admin_user = User(name="System Admin", email="admin@readapt.com", password_hash=hashed_password, role="admin")
    db.session.add(admin_user)
    db.session.commit()
    print("Admin created! Email: admin@readapt.com | Password: admin123")