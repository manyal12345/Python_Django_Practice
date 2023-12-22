# Recursion
# Task requirements (Factorial)
# func(4) -> 4 * 3 * 2 * 1 -> return value

# Decorator
# Task requirements
# Make a list of usernames
# Make a add function , and use login decorator on that function
# The decorator should ask the user for his/her username, if the username is in list print welcome , {username} , else print nothing

# Lambda function
# Task requirments
# Make a lambda function which return multiplication of parameters


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


#Decorator
username = ['admin', 'user1', 'user2', 'user3']

def add(func):
    def wrapper(*args, **kwargs):
        if args in username:
            print(f'Welcome {kwargs["username"]}')
        else:
            print('Nothing')
    return wrapper

@add
def login():
    add(username = 'admin')

login()



#lamda function
add = lambda x, y: x + y
result = add(3, 4)
print(result)