# Single Python program that covers your whole syllabus in simple way

# ---------------------------------------------
# Unit I : Introduction, data types, operators
# ---------------------------------------------

# basic variables (int, float, complex, string, bool)
a = 10               # int
b = 3.5              # float
c = 2 + 3j           # complex
name = "Om"          # string (sequence)
is_student = True    # bool

print("=== Basic variables ===")
print("a =", a, "b =", b, "c =", c, "name =", name, "is_student =", is_student)

# basic operators
sum_ab = a + int(b)          # arithmetic
mul_ab = a * b
is_big = a > 5 and b < 10    # comparison + logical
in_name = "O" in name        # membership on string

print("\n=== Operators ===")
print("sum_ab:", sum_ab)
print("mul_ab:", mul_ab)
print("is_big:", is_big)
print("Does name contain 'O'?", in_name)

# using sequence data types: string, list, tuple
numbers_list = [1, 2, 3]            # list
numbers_tuple = (4, 5, 6)           # tuple

print("\nList:", numbers_list)
print("Tuple:", numbers_tuple)

# ---------------------------------------------
# Unit II : Program flow control + Strings
# ---------------------------------------------

print("\n=== Program flow control & Strings ===")

# read a number from keyboard (also shows input)
user_input = input("Enter a number (for if-elif-else demo): ")

try:
    num = int(user_input)
except ValueError:
    num = 0
    print("Invalid input, taking num = 0")

# conditional blocks
if num > 0:
    msg = "positive"
elif num < 0:
    msg = "negative"
else:
    msg = "zero"

print("Your number is:", msg)

# simple for loop
print("For loop from 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# while loop with break, continue, pass and else
print("\nWhile loop demo (counting 1 to 5, skipping 3):")
x = 0
while x < 5:
    x += 1
    if x == 3:
        # just a placeholder - pass does nothing
        pass
        continue      # skip printing 3
    if x == 5:
        print(x)
        break         # break the loop at 5
    print(x)
else:
    # this will NOT execute because of break
    print("While loop finished without break")

# String handling
print("\n=== String handling ===")
full_name = "Om Singh"

# accessing strings
print("First character:", full_name[0])
print("Last character:", full_name[-1])

# string length
print("Length of full_name:", len(full_name))

# string traversal with for
print("Characters in full_name:")
for ch in full_name:
    print(ch, end=" ")
print()

# string comparison
another_name = "Om singh"
print("full_name == another_name ?", full_name == another_name)

# find function
pos = full_name.find("Singh")
print("Position of 'Singh' in full_name:", pos)

# ---------------------------------------------
# Unit III : Lists and Tuples
# ---------------------------------------------

print("\n=== Lists and Tuples ===")

# list operations
marks = [80, 90, 75]
print("Original marks list:", marks)

marks.append(88)          # add item
print("After append:", marks)

print("Slice marks[1:3]:", marks[1:3])

del marks[0]              # deletion
print("After deleting first element:", marks)

print("Marks using for loop:")
for m in marks:
    print(m, end=" ")
print()

# tuple operations
coords = (10, 20, 30)
print("\nTuple coords:", coords)
print("First coord:", coords[0])
print("Slice coords[1:]:", coords[1:])
print("Length of coords:", len(coords))
print("Count of 20 in coords:", coords.count(20))

# ---------------------------------------------
# Unit IV : Dictionaries and Sets
# ---------------------------------------------

print("\n=== Dictionaries and Sets ===")

# dictionary
student = {
    "name": full_name,
    "age": 20,
    "grades": marks   # list inside dict
}

print("Student dict:", student)
print("Access name:", student["name"])

student["city"] = "Jalandhar"       # add new key
print("After adding city:", student)

print("Loop over dictionary:")
for key, value in student.items():
    print(key, "->", value)

# sets
print("\nSet operations:")
subjects = {"Python", "Maths", "Physics"}
extra_subjects = {"Python", "Chemistry"}

print("subjects:", subjects)
print("extra_subjects:", extra_subjects)

subjects.add("English")           # add item
print("After add:", subjects)

subjects.remove("Maths")          # remove item
print("After remove Maths:", subjects)

print("Looping on set:")
for s in subjects:
    print(s, end=" ")
print()

joined = subjects.union(extra_subjects)   # join sets
print("\nJoined set (union):", joined)

# ---------------------------------------------
# Unit V : Functions and File handling
# ---------------------------------------------

print("\n=== Functions and File handling ===")

# functions

def add_numbers(x, y):   # simple function with arguments
    return x + y

def greet(person_name="Student"):  # default argument
    print("Hello,", person_name)

def analyze_marks(marks_list):
    """Return average marks (small example of function with list)."""
    total = sum(marks_list)
    avg = total / len(marks_list)
    return avg

print("add_numbers(2, 3) =", add_numbers(2, 3))
greet()                  # using default
greet(full_name)         # passing argument

avg_marks = analyze_marks(marks)
print("Average marks:", avg_marks)

# file handling (text file)
print("\nWorking with text file...")
try:
    with open("student_info.txt", "w") as f:
        f.write(f"Name: {full_name}\n")
        f.write(f"Average Marks: {avg_marks}\n")
    print("Data written to student_info.txt")

    with open("student_info.txt", "r") as f:
        content = f.read()
    print("Content of student_info.txt:")
    print(content)
except IOError:
    print("File error occurred!")

# binary file example
print("Working with binary file...")
try:
    with open("sample.bin", "wb") as bf:
        bf.write(b"Hello Binary World")
    with open("sample.bin", "rb") as bf:
        data = bf.read()
    print("Binary data read:", data)
except IOError:
    print("Binary file error occurred!")

# ---------------------------------------------
# Unit VI : Exception handling
# ---------------------------------------------

print("\n=== Exception handling ===")

class NegativeNumberError(Exception):
    """User defined exception."""
    pass

def safe_square(value):
    """Square non-negative integer, raise error otherwise."""
    try:
        n = int(value)
        if n < 0:
            raise NegativeNumberError("Number should not be negative")
        result = n * n
    except ValueError:
        print("ValueError: please enter a valid integer")
        result = None
    except NegativeNumberError as e:
        print("NegativeNumberError:", e)
        result = None
    else:
        print("Square is:", result)
    finally:
        print("safe_square finished (finally block)")
    return result

# nested try example
def demo_nested_try():
    try:
        v = input("Enter a number for safe_square: ")
        try:
            safe_square(v)
        except Exception as e:
            print("Unexpected error inside nested try:", e)
    finally:
        print("Exiting demo_nested_try function")

demo_nested_try()

print("\nProgram finished successfully.")
