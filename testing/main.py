# def do_stuff(num):
#     return num + 5

# after initally testing the code we can make imporvements like these below

def do_stuff(num=0):
    try: 
        if num or num == 0: 
            return int(num) + 5
        else: 
            return 'please enter number'
    except ValueError as err: 
        return err
    