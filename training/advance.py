# Generator function (uses yield)

from functools import wraps


def get_numbers():
    for i in range(5):
        yield i


nums = get_numbers()

print(next(nums))  # 0
print(next(nums))  # 1
print(list(nums))  # [2, 3, 4]

# Using loop
print("*" * 20)
print("Iterate loop")
for line in get_numbers():
    print(line)

# Generator Expression
print("*" * 20)
print("Generator Expression")
squares = [x * x for x in range(5)]
for sqr in squares:
    print(sqr)

# Decorators
# What problem do Decorators solve?
# Decorators allow you to:
# Modify behavior of functions
# Without changing their source code

print("*" * 20)
print("Manually Wrapping a Function")


def greet():
    print("Hello")


def my_wrapper(func):
    def inner():
        print("Before function")
        func()
        print("After function")
    return inner


greet = my_wrapper(greet)
greet()

# Python Decorator Syntax (@)
print("*" * 20)
print("Python Decorator Syntax (@)")


def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper


@my_decorator
def greet():
    print("Hello")


greet()

print("*" * 20)
print("Decorator with Arguments")


def auth_required(func):
    """
    A decorator that reports the execution of a function.
    """

    # to preserve Function Metadata (functools.wraps) of the main function.
    # e.g function name (__name__), docstring (__doc__), and other
    @wraps(func)
    def wrapper(user):  # wrapper is the user define funcation
        """
        Wrapper function docstring (this gets replaced by func's docstring).
        """
        if not user.get("is_logged_in"):
            raise PermissionError("Login required")
        return func(user)
    return wrapper


@auth_required
def dashboard(user):
    """
    Welcome Message.
    """
    print("Welcome!")


dashboard({"is_logged_in": True})

print(f"Function Name: {dashboard.__name__}")
print(f"Docstring: {dashboard.__doc__}")
