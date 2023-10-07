# Reading Tracebacks

The last line is the specific cause of the crash.

```bash
$ python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in ?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
# Cause of the crash
AttributeError: 'int' object has no attribute 'append'
```

However, it's not always easy to read or understand.

_PRO TIP: Paste the whole traceback into Google._
   