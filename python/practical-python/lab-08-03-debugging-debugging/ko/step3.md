# REPL 사용하기

스크립트를 실행할 때 Python 을 유지하려면 `-i` 옵션을 사용하세요.

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

이것은 인터프리터 상태를 유지합니다. 즉, 충돌 후에도 주변을 탐색할 수 있습니다. 변수 값 및 기타 상태를 확인합니다.
