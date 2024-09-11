from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session
from datetime import datetime
from models import storage
from models.user import User
from models.book import Book
from models.review import Review


app = Flask(__name__, template_folder="./templates", static_folder="./static")
app.secret_key = "dev"


@app.route("/")
def dash():
    """handels home page"""

    books = storage.session.query(Book).all()

    return render_template("index.html", books=books)


@app.route("/login", methods=["GET", "POST"])
def login():
    """handels login page"""

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Query the user from the database
        user = storage.session.query(User).filter_by(email=email).first()

        # Check password using hash comparison
        if user and user.password == password:
            session["user_id"] = user.id
            session["username"] = user.user_name
            return redirect(url_for("dash"))
        else:
            print(user, type(user))
            return "Invalid credentials"

    return render_template("login.html")


@app.route("/logout")
def logout():
    """handels logout user"""

    logged_out_user = session.pop("username", None)
    session.pop("user_id", None)
    if logged_out_user:
        flash(f"Good bye {logged_out_user}", "logout")
    return redirect(url_for("dash"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """handels register page"""

    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        dob_str = request.form.get("dob")

        # Check if the email or username already exists
        existing_user = (
            storage.session.query(User)
            .filter((User.email == email) | (User.user_name == username))
            .first()
        )

        if existing_user:
            # If user already exists, return an error message
            flash("Email or username already exists!", "error")
            return render_template("register.html")

        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            flash("Invalid date format. Please use MM/DD/YYYY.", "error")
            return render_template("register.html")

        new_user = User(
            first_name=fname,
            last_name=lname,
            email=email,
            password=password,
            user_name=username,
            date_of_birth=dob,
        )
        new_user.save()
        flash("User added successfully!", "success")
        # time.sleep(5)
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/book/<book_id>")
def book_details(book_id):
    """deliver book details"""

    book = storage.session.query(Book).filter(Book.id == book_id).first()
    return render_template("book_details.html", book=book)


@app.route("/book/<book_id>/add_review", methods=["POST"])
def add_review(book_id):
    """adds review to a book"""

    review_text = request.form.get("user_review")
    if not review_text:
        flash("You must enter a review first", "error")
        return redirect(url_for("book_details", book_id=book_id))

    user_id = session.get("user_id")
    if not session.get("user_id", None):
        flash("You must login first")
        return redirect(url_for("login"))

    book = storage.session.query(Book).filter_by(id=book_id).first()

    new_review = Review(review_text=review_text, book_id=book.id, user_id=user_id)
    storage.session.add(new_review)
    storage.session.commit()

    flash("Your review has been added successfully!", "success")

    return redirect(url_for("book_details", book_id=book_id))


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
