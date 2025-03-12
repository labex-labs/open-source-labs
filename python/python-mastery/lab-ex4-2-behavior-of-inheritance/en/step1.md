# Understanding Single and Multiple Inheritance

In this step, we'll learn about the two main types of inheritance in Python: single inheritance and multiple inheritance. Inheritance is a fundamental concept in object - oriented programming that allows a class to inherit attributes and methods from other classes. We'll also look at how Python determines which method to call when there are multiple candidates, a process known as method resolution.

## Single Inheritance

Single inheritance is when classes form a single line of ancestry. Think of it like a family tree where each class has only one direct parent. Let's create an example to understand how it works.

First, open a new terminal in the WebIDE. Once the terminal is open, start the Python interpreter by typing the following command and then pressing Enter:

```bash
python3
```

Now that you're in the Python interpreter, we'll create three classes that form a single inheritance chain. Enter the following code:

```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()
```

In this code, class `B` inherits from class `A`, and class `C` inherits from class `B`. The `super()` function is used to call the method of the parent class.

After defining these classes, we can find out the order in which Python searches for methods. This order is called the Method Resolution Order (MRO). To see the MRO of class `C`, type the following code:

```python
C.__mro__
```

You should see output similar to this:

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

This output shows that Python first looks for a method in class `C`, then in class `B`, then in class `A`, and finally in the base `object` class.

Now, let's create an instance of class `C` and call its `spam()` method. Type the following code:

```python
c = C()
c.spam()
```

You should see the following output:

```
C.spam
B.spam
A.spam
```

This output demonstrates how `super()` works in a single inheritance chain. When `C.spam()` calls `super().spam()`, it calls `B.spam()`. Then, when `B.spam()` calls `super().spam()`, it calls `A.spam()`.

## Multiple Inheritance

Multiple inheritance allows a class to inherit from more than one parent class. This gives a class access to the attributes and methods of all its parent classes. Let's see how method resolution works in this case.

Enter the following code in your Python interpreter:

```python
class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()
```

Now, we'll create a class `M` that inherits from multiple parent classes `X`, `Y`, and `Z`. Enter the following code:

```python
class M(X, Y, Z):
    pass

M.__mro__
```

You should see the following output:

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

This output shows the Method Resolution Order for class `M`. Python will search for methods in this order.

Let's create an instance of class `M` and call its `spam()` method:

```python
m = M()
m.spam()
```

You should see the following output:

```
X.spam
Y.spam
Z.spam
Base.spam
```

Notice that `super()` doesn't just call the method of the immediate parent class. Instead, it follows the Method Resolution Order (MRO) defined by the child class.

Let's create another class `N` with the parent classes in a different order:

```python
class N(Z, Y, X):
    pass

N.__mro__
```

You should see the following output:

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

Now, create an instance of class `N` and call its `spam()` method:

```python
n = N()
n.spam()
```

You should see the following output:

```
Z.spam
Y.spam
X.spam
Base.spam
```

This shows an important concept: in Python's multiple inheritance, the order of parent classes in the class definition determines the Method Resolution Order. The `super()` function follows this order no matter which class it's called from.

When you're done exploring these concepts, you can exit the Python interpreter by typing the following code:

```python
exit()
```
