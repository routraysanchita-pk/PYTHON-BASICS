# 🐍 DAY 1 - Python Basics Notes

---

# Why Python?

Python is one of the most popular high-level programming languages.

### Features of Python
- Simple and easy to learn.
- Free and open-source.
- High-level programming language.
- Portable (can run on multiple operating systems).
  - Windows
  - macOS
  - Ubuntu/Linux

### Career Opportunities
- Data Science
- Machine Learning
- Artificial Intelligence (AI)
- Web Development (Backend using Django)
- Game Development
- Automation
- Software Development

---

# Python Character Set

Python uses the following types of characters:

### 1. Letters
- A to Z
- a to z

### 2. Digits
- 0 to 9

### 3. Special Symbols
Examples:
```text
+  -  *  /  %  @  #  $  &  !
```

### 4. White Spaces
- Space
- Tab
- New Line
- Carriage Return

### 5. Other Characters
- ASCII Characters
- Unicode Characters

---

# Variables

A **variable** is the name of a memory location used to store data.

## Memory Representation

### Rules for Variables
- Used to store data.
- Created automatically when a value is assigned.
- No need to declare the data type.

### Example

```python
name = "Sandhya"
age = 22
cgpa = 8.6
```

Python automatically decides the data type.

---

# Identifiers

Identifiers are the names given to variables, functions, classes, etc.

## Rules for Identifiers

### 1. Can contain
- Letters (A-Z, a-z)
- Digits (0-9)
- Underscore (_)

Example

```python
student_name
roll1
marks_2025
```

### 2. Cannot start with a digit

❌ Invalid

```python
1name
```

✅ Valid

```python
name1
```

### 3. Special symbols are not allowed

❌ Invalid

```python
student@
marks#
```

### 4. Keywords cannot be used as identifiers

❌ Invalid

```python
if = 10
class = 20
```

### 5. Identifiers should be meaningful

✅ Good

```python
student_name
total_marks
```

CAN BE CONSIDERED BUT NOT MEANINGFUL

```python
a
b
x1
```

---

# Data Types

Python supports different types of data.

## Integer (int)

Whole numbers (positive, negative and zero)

```python
age = 20
marks = -50
```

---

## Float (float)

Decimal values

```python
price = 99.99
pi = 3.14
```

---

## String (str)

Words or sentences enclosed in quotes.

```python
name = "Python"
city = 'Hyderabad'
```

---

## Boolean (bool)

Stores either

```python
True
False
```

Example

```python
is_pass = True
```

---

## None

Represents no value.

```python
data = None
```

---

# Keywords

Keywords are reserved words in Python.

They **cannot be used as identifiers**.

Some Python keywords are:

```text
and
as
assert
break
class
continue
def
del
elif
else
except
False
finally
for
from
global
if
import
in
is
lambda
None
nonlocal
not
or
pass
raise
return
True
try
while
with
yield
```

> Python is a **case-sensitive** language.

Example

```python
Name = "ABC"
name = "XYZ"
```

Both are different variables.

---

# Comments

Comments are parts of the program that are **not executed**.

They make the code easier to understand.

## Single-line Comment

```python
# This is a comment
```

## Multi-line Comment

```python
"""
This is
a multiline
comment.
"""
```

---

# Operators

An operator is a symbol that performs an operation on operands.

Example

```python
a + b
```

- `+` → Operator
- `a` and `b` → Operands

## 1. Arithmetic Operators

```text
+
-
*
/
%
**
```

Example

```python
print(10 + 5)
print(10 % 3)
print(2 ** 3)
```

---

## 2. Relational (Comparison) Operators

```text
==
>
<
>=
<=
!=
```

Example

```python
print(10 > 5)
```

---

## 3. Assignment Operators

```text
=
+=
-=
*=
/=
%=
**=
```

Example

```python
a = 10
a += 5
```

---

## 4. Logical Operators

```text
and
or
not
```

Example

```python
print(True and False)
```

---

# Type Conversion

Type conversion means converting one data type into another.

## 1. Implicit Conversion

Done automatically by Python.

Example

```python
a = 10
b = 2.5

print(a + b)
```

---

## 2. Explicit Conversion (Type Casting)

Done manually by the programmer.

Examples

```python
int("25")

float("12.5")

str(100)
```

---

# Input and Output

## Output

Use the `print()` function to display output.

Example

```python
print("Hello World")
```

---

## Input

The `input()` function accepts input from the user.

```python
name = input("Enter your name: ")
```

**Note:** `input()` always returns a **string**.

---

## Taking Integer Input

```python
age = int(input("Enter age: "))
```

---

## Taking Float Input

```python
salary = float(input("Enter salary: "))
```

---

## Example Program

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)
```

---

# Example Programs

## Hello World

```python
print("Hello World")
```

---

## Sum of Two Numbers

### Method 1

```python
a = 25
b = 25

print(a + b)
```

### Method 2

```python
print(25 + 25)
```

### Method 3

```python
a = 1000
b = 500

sum = a + b

print(sum)
```

---

# DAY - 1 PROGRAMS FOR BETTER REFERENCE

- [📂 DAY1](./DAY1/)

---

# 🐍 DAY 2 - Strings & Conditional Statements

---

# Strings

A **string** is a data type that stores a sequence of characters.

> **Note:** Strings are **immutable**, meaning their characters cannot be modified after creation.

---

# Creating Strings

Strings can be created using:

### Single Quotes

```python
str1 = 'Sanchita'
```

### Double Quotes

```python
str2 = "Sanchita"
```

### Triple Quotes

```python
str3 = """Sanchita"""
```

Triple quotes are generally used for multi-line strings.

---

# Escape Sequence Characters

Escape sequences are special characters used for formatting text.

| Escape Sequence | Meaning |
|----------------|---------|
| `\n` | New Line |
| `\t` | Tab Space |

### Example

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

---

# Operations on Strings

## 1. Concatenation

Joining two or more strings together.

```python
str1 = "Hello"
str2 = "World"

print(str1 + str2)
```

Output

```
HelloWorld
```

---

## 2. Finding Length

The `len()` function returns the length of a string.

```python
str = "Python"

print(len(str))
```

Output

```
6
```

> **Note:** Spaces and special characters are also counted.

Example

```python
print(len("Hello World"))
```

Output

```
11
```

---

# Indexing

Indexing is the process of assigning positions to characters in a string.

Example

```text
String = SANCHITA ROUTRAY

Index:
 S  A  N  C  H  I  T  A     R  O  U  T  R  A  Y
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
```

Accessing characters

```python
str = "SANCHITA"

print(str[0])
```

Output

```
S
```

### Strings are Immutable

```python
str[0] = "B"
```

❌ Not Allowed

You can access characters using indexing, but you cannot modify them.

---

# Slicing

Slicing is used to access a part of a string.

## Syntax

```python
string[start_index : end_index]
```

> The ending index is **not included**.

### Examples

```python
str = "SANCHITA"

print(str[:4])
```

Output

```
SANC
```

```python
print(str[4:])
```

Output

```
HITA
```

Equivalent to

```python
str[4 : len(str)]
```

---

# Negative Indexing

Negative indexing starts from the end of the string.

Example

```text
String = SANCHITA

Index:
-8 -7 -6 -5 -4 -3 -2 -1
 S  A  N  C  H  I  T  A
```

Example

```python
str = "SANCHITA"

print(str[-1])
```

Output

```
A
```

---

# String Functions

Assume

```python
str = "I am a coder"
```

---

## endswith()

Checks whether the string ends with the given substring.

```python
str.endswith("coder")
```

Returns

```
True
```

---

## capitalize()

Capitalizes the first character.

```python
str.capitalize()
```

Output

```
I am a coder
```

---

## replace()

Replaces all occurrences of an old substring with a new substring.

```python
str.replace("coder", "developer")
```

Output

```
I am a developer
```

---

## find()

Returns the index of the first occurrence.

```python
str.find("coder")
```

Output

```
7
```

If not found, it returns **-1**.

---

## count()

Counts the number of occurrences of a substring.

```python
str.count("a")
```

---

# Conditional Statements

Conditional statements are used to make decisions in a program.

---

# if Statement

### Syntax

```python
if condition:
    statement
```

Example

```python
age = 18

if age >= 18:
    print("Eligible to Vote")
```

---

# if-else Statement

### Syntax

```python
if condition:
    statement1
else:
    statement2
```

Example

```python
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# if-elif-else Statement

Used to check multiple conditions.

### Syntax

```python
if condition1:
    statement1

elif condition2:
    statement2

...

else:
    statementN
```

Example

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
```

---

# Nested if-else Statement

A **nested if-else** statement means placing one `if` statement inside another `if` or `else` block. It is used when multiple conditions depend on one another.

## Syntax

```python
if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3
```

---

## Example 1: Check Positive and Even Number

```python
num = 12

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")
```

### Output

```text
Positive Even Number
```

---

## Example 2: Eligibility for Scholarship

```python
marks = 85

if marks >= 50:
    if marks >= 80:
        print("Eligible for Scholarship")
    else:
        print("Passed but Not Eligible for Scholarship")
else:
    print("Failed")
```

### Output

```text
Eligible for Scholarship
```
> **Note:** Use **nested `if-else`** when one condition needs to be checked only after another condition is satisfied.

---

# DAY - 2 PROGRAMS FOR BETTER REFERENCE

- [📂 DAY2](./DAY2/)

---

# 🐍 Day 3: Lists & Tuples

---

# Lists

A **list** is a built-in data type that stores a collection of values.

Lists can store elements of **different data types** (int, float, string, etc.) together.

## Creating a List

```python
marks = [95, 87, 20, 19, 76]
```

---

## Accessing Elements

Use the index of the element.

### Syntax

```python
list_name[index]
```

### Example

```python
marks[0]
```

Output

```text
95
```

---

## Finding Length of a List

Use the `len()` function.

### Syntax

```python
len(list_name)
```

### Example

```python
len(marks)
```

Output

```text
5
```

---

## List with Multiple Data Types

Lists can store different data types together.

```python
student = ["Karan", 19, "Delhi"]
```

---

## Lists are Mutable

Lists are mutable, meaning their elements can be modified.

### Example

```python
student = ["Karan", 19, "Delhi"]

student[0] = "Arjun"

print(student)
```

Output

```python
['Arjun', 19, 'Delhi']
```

---

## List Slicing

List slicing works the same way as string slicing.

### Syntax

```python
list_name[start_index:end_index]
```

Example

```python
marks = [95, 87, 20, 19, 76]

print(marks[1:4])
```

Output

```python
[87, 20, 19]
```

---

# List Methods

Assume

```python
lst = [2, 1, 3]
```

---

## append()

Adds one element to the end of the list.

```python
lst.append(4)
```

Output

```python
[2, 1, 3, 4]
```

---

## sort()

Sorts the list in ascending order.

```python
lst.sort()
```

Output

```python
[1, 2, 3]
```

---

## sort(reverse=True)

Sorts the list in descending order.

```python
lst.sort(reverse=True)
```

Output

```python
[3, 2, 1]
```

---

## reverse()

Reverses the list.

```python
lst.reverse()
```

---

## insert()

Inserts an element at the given index.

### Syntax

```python
lst.insert(index, element)
```

Example

```python
lst.insert(1, 10)
```

Output

```python
[2, 10, 1, 3]
```

---

## remove()

Removes the first occurrence of an element.

```python
lst.remove(1)
```

---

## pop()

Removes the element at the given index.

```python
lst.pop(2)
```

---

## Important Note

```python
lst = [3, 1, 2]

print(lst.sort())
```

Output

```text
None
```

Because `sort()` modifies the original list and returns nothing.

Correct way:

```python
lst.sort()
print(lst)
```

Output

```python
[1, 2, 3]
```

---

# Tuples

A **tuple** is a built-in data type used to store an immutable sequence of values.

### Creating a Tuple

```python
marks = (87, 64, 98, 51, 29)
```

---

## Tuples are Immutable

Tuple elements **cannot be modified**.

```python
marks[1] = 2
```

❌ This operation is not allowed.

---

## Accessing Tuple Elements

### Syntax

```python
tuple_name[index]
```

### Example

```python
marks[0]
```

Output

```text
87
```

---

## Length of a Tuple

Use the `len()` function.

```python
len(marks)
```

Output

```text
5
```

---

## Single Value Tuple

When creating a tuple with only one element, a comma **must** be used.

```python
marks = (87,)
```

Without the comma,

```python
marks = (87)
```

Python treats it as an integer, **not** a tuple.

---

## Tuple Slicing

Tuple slicing works exactly like list slicing.

### Example

```python
marks = (87, 64, 98, 51, 29)

print(marks[1:4])
```

Output

```python
(64, 98, 51)
```

---

## Tuple with Different Data Types

A tuple can store different types of values together.

```python
student = ("Sanchita", 22, "Cuttack", 9.02)
```

---

# Tuple Methods

Assume

```python
tup = (2, 1, 3, 1)
```

---

## index()

Returns the index of the first occurrence of an element.

```python
tup.index(1)
```

Output

```text
1
```

---

## count()

Returns the total number of occurrences of an element.

```python
tup.count(1)
```

Output

```text
2
```

---

# Difference Between List and Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can be modified | Cannot be modified |
| More methods available | Fewer methods available |

---

# DAY - 3 PROGRAMS FOR BETTER REFERENCE

- [📂 DAY3](./DAY3/)
