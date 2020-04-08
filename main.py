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
        donor_name = request.form['name']
        donation_amount = request.form['donation']

        # Find the donor
        donor = Donor.select().where(Donor.name == donor_name).get()

        #donation
        donation = Donation(value = donation_amount, donor = donor)
        donation.save()
        return redirect(url_for('all'))
    else:
        return render_template('create.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
