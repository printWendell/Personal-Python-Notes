# from utility import multiply, divide
# import shopping.more_shopping.shopping_cart
# from shopping.more_shopping.shopping_cart import buy
# from random import shuffle

# my_list = [1, 2, 3, 4, 5]
# shuffle(my_list)

# if __name__ == '__main__': 
#     print(buy('fruit'))
#     print(divide(5, 2))
#     print(multiply(5, 2))
#     print('please run')
#     print(my_list)

from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li = [1, 2, 3, 4, 5, 6, 7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist',{
    'a': 1,
    'b': 2
})

print(dictionary['f'])


# python3.7+ recently made dictionaries ordered by default
d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

d3 = OrderedDict()
d3['a'] = 1
d3['b'] = 2

print(d2 == d3) #true

print(datetime.date.today())

# python arrays take in a typecode parameter
array('i', [1, 3, 4])
