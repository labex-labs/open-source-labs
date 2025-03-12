# Understanding Single and Multiple Inheritance

In this step, we will explore the two primary "directions" of inheritance in Python: single inheritance and multiple inheritance. We'll examine how method resolution works in both cases.

## Single Inheritance

Single inheritance occurs when classes form a single line of ancestry. Let's create an example to see how it works.

Open a new terminal in the WebIDE and start the Python interpreter by typing:

```bash
python3
```

Now, enter the following code to create three classes with a single inheritance chain:

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

After defining these classes, we can examine how Python determines the method resolution order (MRO) and how `super()` navigates this order:

```python
C.__mro__
```

You should see output similar to:

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

This shows the order in which Python searches for methods. Now, let's create an instance of class `C` and call its `spam()` method:

```python
c = C()
c.spam()
```

You should see:

```
C.spam
B.spam
A.spam
```

This demonstrates how `super()` works in a single inheritance chain. When `C.spam()` calls `super().spam()`, it calls `B.spam()`. Then, when `B.spam()` calls `super().spam()`, it calls `A.spam()`.

## Multiple Inheritance

Multiple inheritance allows a class to inherit from more than one parent class. Let's see how method resolution works in this case. Enter the following code in your Python interpreter:

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

Now, let's create a class that inherits from multiple parent classes:

```python
class M(X, Y, Z):
    pass

M.__mro__
```

You should see:

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

Let's create an instance and call the `spam()` method:

```python
m = M()
m.spam()
```

You should see:

```
X.spam
Y.spam
Z.spam
Base.spam
```

Notice how `super()` doesn't simply call the immediate parent class's method. Instead, it follows the Method Resolution Order (MRO) defined by the child class.

Let's create another class with the parents in a different order:

```python
class N(Z, Y, X):
    pass

N.__mro__
```

You should see:

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

Now call the `spam()` method on an instance of `N`:

```python
n = N()
n.spam()
```

You should see:

```
Z.spam
Y.spam
X.spam
Base.spam
```

This demonstrates an important concept: in Python's multiple inheritance, the order of parent classes in the class definition determines the Method Resolution Order. The `super()` function follows this order regardless of which class it's called from.

You can exit the Python interpreter when you're done:

```python
exit()
```
