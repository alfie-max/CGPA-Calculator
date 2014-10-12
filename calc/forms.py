from wtforms import Form, TextField, SubmitField, validators, ValidationError

class CalcForm(Form):
    c_range  = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
    c_error  = u"Invalid entry. Maximum credit allowed is 10"
    g_range  = ['S','s', 'A','a', 'B','b', 'C','c', 'D','d', 'E','e', 'U','u']
    g_error  = u"Invalid Entry. Valid grades are [ S,A,B,C,D,E,U ]"
    
    # Semester 1 & 2
    c_101   = c_102  = c_103  = c_103P  = \
    c_104   = c_104P = c_105  = c_106   = \
    c_107   = c_108  = c_109P = c_110AP = \
    c_110BP = TextField([validators.AnyOf(values = c_range, message = c_error)])
    
    g_101   = g_102  = g_103  = g_103P  = \
    g_104   = g_104P = g_105  = g_106   = \
    g_107   = g_108  = g_109P = g_110AP = \
    g_110BP = TextField([validators.AnyOf(values = g_range, message = g_error)])

    # Semester 3
    c_301  = c_302 = c_303  = c_304  = \
    c_305  = c_306 = c_307P = c_308P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    g_301  = g_302 = g_303  = g_304  = \
    g_305  = g_306 = g_307P = g_308P = TextField([validators.AnyOf(values = g_range, message = g_error)])

    # Semester 4
    c_401  = c_402 = c_403  = c_404  = \
    c_405  = c_406 = c_407P = c_408P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    g_401  = g_402 = g_403  = g_404  = \
    g_405  = g_406 = g_407P = g_408P = TextField([validators.AnyOf(values = g_range, message = g_error)])

    # Semester 5
    c_501  = c_502 = c_503  = c_504  = \
    c_505  = c_506 = c_507P = c_508P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    g_501  = g_502 = g_503  = g_504  = \
    g_505  = g_506 = g_507P = g_508P = TextField([validators.AnyOf(values = g_range, message = g_error)])

    # Semester 6
    c_601  = c_602 = c_603  = c_604  = \
    c_605  = c_606 = c_607P = c_608P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    g_601  = g_602 = g_603  = g_604  = \
    g_605  = g_606 = g_607P = g_608P = TextField([validators.AnyOf(values = g_range, message = g_error)])

    # Semester 7
    c_701  = c_702  = c_703  = c_704  = \
    c_705  = c_706  = c_707P = c_708P = \
    c_709P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    g_701  = g_702  = g_703  = g_704  = \
    g_705  = g_706  = g_707P = g_708P = \
    g_709P = TextField([validators.AnyOf(values = g_range, message = g_error)])

    # Semester 8
    c_801  = c_802  = c_803  = c_804 = \
    c_805P = c_806P = c_807P = TextField([validators.AnyOf(values = c_range, message = c_error)])

    g_801  = g_802  = g_803  = g_804 = \
    g_805P = g_806P = g_807P = TextField([validators.AnyOf(values = g_range, message = g_error)])

    # Calculate Button
    submit = SubmitField("Calculate")
