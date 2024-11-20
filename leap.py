def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    four = year % 4
    if four == 0:
        one_hundred = year % 100
        if one_hundred == 0:
            four_hundred = year % 400
            if four_hundred == 0:
                print('yes it is divisible by 400')
            else:
                print('no')
        else: print('yes its divisible by 4 and not 100 ')
    else:
        print('no its not divisible by 4')

is_leap_year(2100)
