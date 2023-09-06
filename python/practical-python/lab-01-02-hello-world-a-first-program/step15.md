# Printing

The `print` function produces a single line of text with the values passed.

```python
print('Hello world!') # Prints the text 'Hello world!'
```

You can use variables. The text printed will be the value of the variable, not the name.

```python
x = 100
print(x) # Prints the text '100'
```

If you pass more than one value to `print` they are separated by spaces.

```python
name = 'Jake'
print('My name is', name) # Print the text 'My name is Jake'
```

`print()` always puts a newline at the end.

```python
print('Hello')
print('My name is', 'Jake')
```

This prints:

```code
Hello
My name is Jake
```

The extra newline can be suppressed:

```python
print('Hello', end=' ')
print('My name is', 'Jake')
```

This code will now print:

```code
Hello My name is Jake
```

