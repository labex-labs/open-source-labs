# 예외 처리 (Exception Handling)

예외는 첫 번째 일치하는 `except`로 전파됩니다.

```python
def grok():
    ...
    raise RuntimeError('Whoa!')   # Exception raised here

def spam():
    grok()                        # Call that will raise exception

def bar():
    try:
       spam()
    except RuntimeError as e:     # Exception caught here
        ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # Exception does NOT arrive here
        ...

foo()
```

예외를 처리하려면, `except` 블록 안에 문을 넣으십시오. 오류를 처리하기 위해 원하는 모든 문을 추가할 수 있습니다.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements              # Use this statements
        statements
        ...

bar()
```

처리가 완료된 후, 실행은 `try-except` 뒤의 첫 번째 문으로 재개됩니다.

```python
def grok(): ...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements
        statements
        ...
    statements                  # Resumes execution here
    statements                  # And continues here
    ...

bar()
```
