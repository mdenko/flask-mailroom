import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session
from playhouse.db_url import connect
from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))
        db.connect()
        new_donation = {'name': request.form['name'], 'value':request.form['donation']}
        donations = dict(Donation.select())
        donations.append(new_donation)
        return render_template('donations.jinja2', donations=donations)
    else:
        return render_template('create.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
