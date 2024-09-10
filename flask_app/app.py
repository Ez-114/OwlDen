from flask import Flask, render_template, request, redirect, url_for, flash
import time
from datetime import datetime
from models import storage
from models.user import User


app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.secret_key = 'dev'


@app.route('/')
def dash():
    """handels home page"""

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """handels login page"""

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the user from the database
        user = storage.session.query(User).filter_by(email=email).first()

        # Check password using hash comparison
        if user and user.password == password:
            return redirect(url_for('dash'))
        else:
            print(user, type(user))
            return "Invalid credentials"

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """handels register page"""

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        username = request.form.get('password')
        email = request.form.get('email')
        password = request.form.get('password')
        dob_str = request.form.get('dob')

        # Check if the email or username already exists
        existing_user = storage.session.query(User).filter(
            (User.email == email) | (User.user_name == username)
        ).first()

        if existing_user:
            # If user already exists, return an error message
            flash('Email or username already exists!', 'error')
            return render_template('register.html')

        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format. Please use MM/DD/YYYY.', 'error')
            return render_template('register.html')

        new_user = User(
            first_name=fname,
            last_name=lname,
            email=email,
            password=password,
            user_name=username,
            date_of_birth=dob
        )
        new_user.save()
        flash('User added successfully!', 'success')
        # time.sleep(5)
        return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
