from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean = True)
  
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
  
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email1 = request.form.get('email1')
        email2 = request.form.get('email2')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        university = request.form.get('university')
        
        if len(email1) < 4:
            flash("Email is too short", category="error")
            return render_template("sign_up.html")
        elif len(firstName) < 2:
            flash("First name is too short", category="error")
            return render_template("sign_up.html")
        elif len(lastName) < 2:
            flash("Last name is too short", category="error")
            return render_template("sign_up.html")
        elif email1 != email2:
            flash("Emails don't match", category="error")
            return render_template("sign_up.html")
        elif len(password1) < 8:
            flash("Password is too short", category="error")
            return render_template("sign_up.html")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
            return render_template("sign_up.html")
        else:
            flash("Account created", category="success")
            # add user to database
            return render_template("sign_up.html")
    return render_template("sign_up.html")
