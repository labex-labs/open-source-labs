# Чтение трассировок стека

Последняя строка - это конкретная причина аварии.

```bash
$ python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
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

Однако, не всегда легко прочитать или понять.

_ПРО-ТИП: Вставьте всю трассировку стека в Google._
