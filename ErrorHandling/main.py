# Error Handling

while True: 
    try: 
        age = int(input('what is your age? '))
        10/age
        # raise stops the program
        raise ValueError('hey cut it')
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than zero')
        break
    # else is only executed when there is no exeption
    else: 
        print('thank you')
        break;
    # finally will run no matter what
    finally: 
        print('ok, im finally done')
    print('can you hear me?')

# def sum(num1, num2): 
#     try: 
#         return num1/ num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err) 

# print(sum('1',2))