# define functions
def num_to_month(value_tuple):
    ii = 0
    value_new = [0,0]
    for i in value_tuple:
        if i == 1:
            month_str = 'January'
        elif i == 2:
            month_str = 'February'
        elif i == 3:
            month_str = 'March'
        elif i == 4:
            month_str = 'April'
        elif i == 5:
            month_str = 'May'
        elif i == 6:
            month_str = 'June'
        elif i == 7:
            month_str = 'July'
        if i == 8:
            month_str = 'August'
        elif i == 9:
            month_str = 'September    '
        elif i == 10:
            month_str = 'October'
        elif i == 11:
            month_str = 'November'
        elif i == 12:
            month_str = 'December'
        else:
            print('')
        value_new[ii] = month_str
        ii = ii + 1
    return value_new

