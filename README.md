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

#### Code Samples

a = 4
b = 11
print(a | b)
print(a >> 2)

output:
15
1

Explanation:
Bitwise right shift operator(>>): The a’s value is moved right by the 2 bits.

x = 100
y = 50
print(x and y)

output:
50

Explanation:
In Python, When we join two non-Boolean values using a and operator, the value of the expression is the second operands, not True or False.

a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)

output:
[10, 20, 30, 40]
[10, 20, 30, 40]

Explanation:
Because both b and a refer to the same object, when we use addition assignment += on b, it changes both a and b
