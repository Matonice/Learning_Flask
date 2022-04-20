from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                    SelectField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired
app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

class InfoForm(FlaskForm):

    breed = StringField("What breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose your mode:", choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField('Pick your favorite food: ',
                                choices=[('chi', 'chicken'), ('bf', 'beef'), ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thank_you'))
    return render_template('index.html', form=form)

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
