from contextlib import contextmanager

f = open("hello.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

# Reading a File
print("# Reading a File")
file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()

# Writing a File
with open("hello.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")


# Using with Statement
# with Statement in Python simplifies resource management by automatically handling setup and cleanup, ensuring files or connections close safely even if errors occur.
# Replaces long try-except–finally blocks with cleaner syntax.
# Improves readability by reducing unnecessary boilerplate code.
# Example
print('# Without "with" (Manual closing)')
file = open("hello.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensures the file is closed

# Using "with" (Automatic closing)
print('# Using "with" (Automatic closing)')
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)  # File closes automatically

# Writing to a file
print("# Writing to a file")
with open("hello.txt", "w") as file:
    file.write("Hello, Python with statement!")

# Context Managers
# is an object that guarantees the proper setup and teardown of resources,
# such as files, network connections, and locks. It simplifies code by
# replacing repetitive try...finally blocks with the cleaner with statement.
# manage resource allocation and deallocation using two special methods:
# - __enter__(): Acquires the resource and returns it.
# - __exit__(): Releases the resource when the block exits


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# using the custom context manager
with FileManager("hello.txt", "w") as file:
    file.write("Hello, World!")


# Using contextlib Module
# Function-Based Context Manager
@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()


# Using the generator-based context manager
with open_file("hello.txt", "w") as file:
    file.write("Hello, World! with contextlib Module")
