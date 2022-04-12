from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/club_home')
def club_home():
    return render_template('club_home.html')

@app.route('/club_index')
def club_index():
    return render_template('club_index.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('/')
@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/clubs')
def clubs():
    return render_template('clubs.html')

if __name__ == '__main__':
    app.run()
