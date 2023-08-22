from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from database import get_posts

app = Flask(__name__)
# ! should set up a secret key to prevent attacks with cookies 

# dummy data
# list of dictionaries, mimics database 
posts_old = [
    {
        'author': 'Jane Doe',
        'title': 'About me',
        'content': 'Hi my name is...',
        'date_posted': 'June 26, 2023'
    }, 
    {
        'author': 'Jennie Kim',
        'title': 'Daily Life',
        'content': 'Today...',
        'date_posted': 'June 30, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=get_posts())

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # testing log in
    # if we submitted the form 
    if form.validate_on_submit():
        # checking if its the email and pass we want 
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            # flash 
            # category is just the type of bootstrap class we want the flash message to have 
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful', 'danger')
    return render_template('login.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True)