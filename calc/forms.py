from wtforms import Form, TextField, SubmitField, validators, ValidationError

class WelcomeForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name")])
    submit = SubmitField("Submit")

class CalcForm(Form):
    submit = SubmitField("Calculate")
