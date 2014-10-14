from wtforms import Form, TextField, SubmitField, validators, ValidationError

class WelcomeForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    submit = SubmitField("Submit")

class CalcForm(Form):
    c_range  = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
    c_error  = u"Invalid entry. Maximum credit allowed is 10"
    
    # Semester 1 & 2
    c_101   = c_102  = c_103  = c_103P  = \
    c_104   = c_104P = c_105  = c_106   = \
    c_107   = c_108  = c_109P = c_110AP = \
    c_110BP = TextField([validators.AnyOf(values = c_range, message = c_error)])

    # Semester 3
    c_301  = c_302 = c_303  = c_304  = \
    c_305  = c_306 = c_307P = c_308P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    # Semester 4
    c_401  = c_402 = c_403  = c_404  = \
    c_405  = c_406 = c_407P = c_408P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    # Semester 5
    c_501  = c_502 = c_503  = c_504  = \
    c_505  = c_506 = c_507P = c_508P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    # Semester 6
    c_601  = c_602 = c_603  = c_604  = \
    c_605  = c_L01 = c_607P = c_608P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    # Semester 7
    c_701  = c_702  = c_703  = c_704  = \
    c_L02  = c_L03  = c_707P = c_708P = \
    c_709P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    # Semester 8
    c_801  = c_802  = c_L04  = c_L05 = \
    c_805P = c_806P = c_807P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    # Calculate Button
    submit = SubmitField("Calculate")
