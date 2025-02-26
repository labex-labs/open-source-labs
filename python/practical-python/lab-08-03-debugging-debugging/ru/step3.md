# Использование интерактивного интерпретатора Python (REPL)

Используйте параметр `-i`, чтобы запустить скрипт и оставить Python запущенным.

```bash
$ python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
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

Это сохраняет состояние интерпретатора. Это означает, что вы можете исследовать состояние программы после аварии. Проверять значения переменных и другое состояние.
