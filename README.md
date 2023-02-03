# Python Training

### Guides & Environment Setup

- [Python](https://www.python.org/)
- [Detailed Python Setup and Usage](https://docs.python.org/3.10/using/index.html)
- [PIP Installation doc](https://pip.pypa.io/en/stable/installation/)
- [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- Visual Studio Code Python extension

### Python Intro

Linkedin Learning -> [Learning Python](https://www.linkedin.com/learning/learning-python-14393370)(Exercises: https://github.com/LinkedInLearning/learning-python-2896241)

### Python Theoretical Quiz (Multiple choice)

#### [Pynative Quizes](https://pynative.com/python/quizzes/)

- [Basic Python Quiz For Beginners](https://pynative.com/basic-python-quiz-for-beginners/)

- [Python Variables and Data Types Quiz](https://pynative.com/python-variables-and-data-types-quiz/)
- [Python Operators and Expressions Quiz](https://pynative.com/python-operators-and-expression-quiz/)
- [Python Input and Output Quiz](https://pynative.com/python-input-and-output-quiz/)
- [Python Functions Quiz](https://pynative.com/python-functions-quiz/)
- [Python If Else and Loops Quiz](https://pynative.com/python-if-else-and-for-loop-quiz/)

## Notes

### Variables and Data types

Sample
str1 = 'Ault\'Kelly'
str1 = """Ault'Kelly"""

output:
Ault'Kelly

### Python operators

// Floor division)
℅ (Modulus)
\*\* (Exponentiation)

Priority

Precedence level Operator Meaning
1 (Highest) () Parenthesis
2 \*_ Exponent
3 +x, -x ,~x Unary plus, Unary Minus, Bitwise negation
4 _, /, //, % Multiplication, Division, Floor division, Modulus
5 +, - Addition, Subtraction
6 <<, >> Bitwise shift operator
7 & Bitwise AND
8 ^ Bitwise XOR
9 | Bitwise OR
10 ==, !=, >, >=, <, <= Comparison
11 is, is not, in, not in Identity, Membership
12 not Logical NOT
13 and Logical AND
14 (Lowest) or Logical OR

#### **Code Samples**

```python
a = 4
b = 11
print(a | b)
print(a >> 2)
```

output:

```text
15
1
```

**Explanation**:
Bitwise right shift operator(>>): The a’s value is moved right by the 2 bits.

```python
x = 100
y = 50
print(x and y)
```

output:

```text
50
```

**Explanation**:
In Python, When we join two non-Boolean values using a and operator, the value of the expression is the second operands, not True or False.

```python
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)
```

output:

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

**Explanation**:
Because both b and a refer to the same object, when we use addition assignment += on b, it changes both a and b

### **File Handling**

![Alt text](https://pynative.com/wp-content/uploads/2021/07/file_handling_in_python.png "Title")

**File Access Modes**

<table>
<thead>
<tr>
<th><strong>Mode</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>r</code></td>
<td>It opens an existing file to read-only mode. The file pointer exists at the beginning.</td>
</tr>
<tr>
<td><code>rb</code></td>
<td>It opens the file to read-only in binary format. The file pointer exists at the beginning.</td>
</tr>
<tr>
<td><code>r+</code></td>
<td>It opens the file to read and write both. The file pointer exists at the beginning.</td>
</tr>
<tr>
<td><code>rb+</code></td>
<td>It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.</td>
</tr>
<tr>
<td><code>w</code></td>
<td>It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name.</td>
</tr>
<tr>
<td><code>wb</code></td>
<td>It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists.</td>
</tr>
<tr>
<td><code>w+</code></td>
<td>It opens the file to write and read data. It will override existing data.</td>
</tr>
<tr>
<td><code>wb+</code></td>
<td>It opens the file to write and read both in binary format</td>
</tr>
<tr>
<td><code>a</code></td>
<td>It opens the file in the append mode. It will not override existing data. It creates a new file if no file exists with the same name.</td>
</tr>
<tr>
<td><code>ab</code></td>
<td>It opens the file in the append mode in binary format.</td>
</tr>
<tr>
<td><code>a+</code></td>
<td>It opens a file to append and read both.</td>
</tr>
<tr>
<td><code>ab+</code></td>
<td>It opens a file to append and read both in binary format.</td>
</tr>
</tbody>
</table>

#### **Writing File**

```python
text = "This is new content"
# writing new content to the file
fp = open("write_demo.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()
```

#### **File Methods**

<table>
<thead>
<tr>
<th><strong>Mode</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>r</code></td>
<td>It opens an existing file to read-only mode. The file pointer exists at the beginning.</td>
</tr>
<tr>
<td><code>rb</code></td>
<td>It opens the file to read-only in binary format. The file pointer exists at the beginning.</td>
</tr>
<tr>
<td><code>r+</code></td>
<td>It opens the file to read and write both. The file pointer exists at the beginning.</td>
</tr>
<tr>
<td><code>rb+</code></td>
<td>It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.</td>
</tr>
<tr>
<td><code>w</code></td>
<td>It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name.</td>
</tr>
<tr>
<td><code>wb</code></td>
<td>It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists.</td>
</tr>
<tr>
<td><code>w+</code></td>
<td>It opens the file to write and read data. It will override existing data.</td>
</tr>
<tr>
<td><code>wb+</code></td>
<td>It opens the file to write and read both in binary format</td>
</tr>
<tr>
<td><code>a</code></td>
<td>It opens the file in the append mode. It will not override existing data. It creates a new file if no file exists with the same name.</td>
</tr>
<tr>
<td><code>ab</code></td>
<td>It opens the file in the append mode in binary format.</td>
</tr>
<tr>
<td><code>a+</code></td>
<td>It opens a file to append and read both.</td>
</tr>
<tr>
<td><code>ab+</code></td>
<td>It opens a file to append and read both in binary format.</td>
</tr>
</tbody>
</table>

### **Functions**

Sample 1

```python
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)
```

Solution

```python
15
```

Sample 2

```python
def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)
```

```python
Emma 25
```

Explanation:

We can specify default values for arguments when defining a function. the function uses the default value if the value for an argument is missing in a function call.

Sample 3

```python
def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)
```

```python
emp
salary
```

Explanation:

To accept Variable Length of Keyword Arguments, i.e., To create functions that take n number of Keyword arguments we use **kwargs (prefix a parameter name with a double asterisk ** ).

keyword arguments: display(emp="Kelly", salary=9000)

This \*\*kwargs collects all passed arguments into a new dictionary, where the argument names are the keys, and their values are the key’s values.

So to get the values we need to iterate the kwargs dictionary like this

Sample 4

```python
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)
```

```python
(8, 7)
```

Explanation:

In Python, we can return multiple values from a function. You can do this by separating return values with a comma.

```python

```

```python

```

```python

```

```python

```
