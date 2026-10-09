try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    num = int("hello")
except ValueError:
    print("Invalid number")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Index does not exist")

try:
    student = {"name": "Priya"}
    print(student["age"])
except KeyError:
    print("Key not found")

try:
    print("Age: " + 20)
except TypeError:
    print("Different data types")

try:
    file = open("test.txt")
except FileNotFoundError:
    print("File not found")

try:
    print(x)
except NameError:
    print("Variable does not exist")

try:
    print(10 / 0)
except Exception as e:
    print("An error occurred:", e)

try:
    print(10 / 2)
except:
    print("Error")
finally:
    print("This always runs")


try:
    number = 10
    number.append(5)
except AttributeError:
    print("This object does not have that attribute")

try:
    import something_that_does_not_exist
except ImportError:
    print("Module not found")


try:
    file = open("protected_file.txt", "w")
except PermissionError:
    print("You do not have permission")