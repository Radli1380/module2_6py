def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
def print_params(a = 1, b = 'строка'):
    print(a, b,)

print_params()
def print_params( b = 25,c= [1,2,3]):
    print(b, c,)

print_params()



def print_params(a , b, c):
    print(a, b,c )

values_list = (1, 'string', [1, 2, 3])
print_params(*values_list)

def print_params(a , b, c):
    print(a, b,c )

value_dict = {'a':1, 'b': 'строка', 'c': True}
print_params(**value_dict)

def print_params(a , b, c):
    print(a, b,c )

value_list_2 = [54.32, 'string']
print_params(*value_list_2, 42)





