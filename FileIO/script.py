# my_file = open('test.txt')

# # print(my_file.read())
# print(my_file.readlines())

# my_file.close()

# modes
# r = 'read'
# w = 'write' - write to a file/adds to beginning of file/overrides the text/ can create new files
# a = 'append' - 'adds to end of file'

# r+ = 'read and write' doesnt overrite text/ cant create new files
try:         
    with open('../testFolder/sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err: 
    print('file does not exist')
    raise err
except IOError as err: 
    print('IO error')
    raise err