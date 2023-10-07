# Using the REPL

Use the option `-i` to keep Python alive when executing a script.

```bash
$ python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>
```

It preserves the interpreter state. That means that you can go poking around after the crash. Checking variable values and other state.
