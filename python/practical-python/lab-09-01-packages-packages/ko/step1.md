# 모듈 (Modules)

모든 Python 소스 파일은 모듈입니다.

```python
# foo.py
def grok(a):
    ...
def spam(b):
    ...
```

`import` 문은 모듈을 로드하고 *실행*합니다.

```python
# program.py
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```
