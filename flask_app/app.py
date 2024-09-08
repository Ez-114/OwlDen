from flask import Flask, render_template, request, redirect, url_for
from models import storage
from models.user import User


app = Flask(__name__, template_folder='./templates', static_folder='./static')


@app.route('/')
def dash():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
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

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
