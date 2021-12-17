from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os
from flask import render_template, redirect, url_for, jsonify
from flask_wtf import FlaskForm

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

app = Flask('__name__')
app.config['SECRET_KEY'] = 'ty4425hk54a21eee5719b9s9df7sdfklx'
csrf.init_app(app)



class RegistrationForm(Form):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('Address1', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    city_name = StringField('cityname', validators=[DataRequired()])
    states = SelectField('States', choices=[('BK', 'CT'), ('CK', 'AP')])





@app.route('/')
def index():
    form = RegistrationForm()
    return render_template('registration.html', form=form)

@app.route('/register', methods = ['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print('Submission successful')
        return redirect(url_for('index'))
    
    return render_template('registration.html', form=form)

if __name__ == "__main__":
    app.run(debug=True,port=5006)