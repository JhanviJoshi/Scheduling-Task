from datetime import datetime

from flask import flash
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, DateTimeField, StringField, DateField
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired, Required, InputRequired


def check_date(form,field):

    # date_format = '%d-%m-%Y'
    field1 = str(field)
    try:
        d,m,y = map(int,field1.split("-"))
        # date_time = field.strftime( '%d-%m-%Y')
        # date_obj = datetime.strptime(str(field), date_format)
        # print(date_obj)
    except ValueError:
        print("except")
        flash("Date should be in dd-mm-YYYY")
        raise ValidationError("Date should be in dd-mm-YYYY")



class ContactForm(FlaskForm):


    profile = StringField("PROFILE", [InputRequired()])
    startdate = StringField("STARTDATE",[InputRequired(), check_date])
    enddate = DateTimeField("ENDDATE",[InputRequired()])
    user = StringField("USER", [InputRequired()])

    submit = SubmitField("Submit")