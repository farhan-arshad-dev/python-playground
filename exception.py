# Handel Exception

try:
    n = 0
    res = 100 / n

except ZeroDivisionError:
    print("You can't divide by zero!")

except (ValueError, TypeError):
    print("Enter a valid number!")

except IndexError:
    print("Index out of range.")

except:  # Catch-All Handlers and Their Risks
    print("Something went wrong!")

else:
    print("Result is", res)

finally:
    print("Execution complete.")


# Raise an Exception
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")


try:
    set(-5)
except ValueError as e:
    print(e)

# Custom Exceptions
print("# Custom Exceptions")


class AgeError(Exception):
    pass


def set(age):
    if age < 0:
        raise AgeError("Age cannot be negative.")
    print(f"Age set to {age}")


try:
    set(-5)
except AgeError as e:
    print(e)
