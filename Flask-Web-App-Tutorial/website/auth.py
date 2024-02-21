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
        
        if email1 < 4:
            flash("Email is too short", category="error")
            pass
        elif firstName < 2:
            flash("First name is too short", category="error")
            pass
        elif lastName < 2:
            flash("Last name is too short", category="error")
            pass
        elif email1 != email2:
            flash("Emails don't match", category="error")
            pass
        elif password1 < 8:
            flash("Password is too short", category="error")
            pass
        elif password1 != password2:
            flash("Passwords don't match", category="error")
            pass
        else:
            flash("Account created", category="success")
            # add user to database
            pass
    return render_template("sign_up.html")
