# Returning Multiple Values

Suppose you were writing code to parse configuration files consisting of lines like this:

    name=value

Write a function `parse_line(line)` that takes such a line and returns both the associated name and
value. The common convention for returning multiple values is to return them in a tuple. For example:

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> name, val = parse_line('email=guido@python.org')
>>> name
'email'
>>> val
'guido@python.org'
>>>
```
