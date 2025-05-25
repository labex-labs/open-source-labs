# 딕셔너리와 모듈

모듈 내에서 딕셔너리는 모든 전역 변수와 함수를 저장합니다.

```python
# foo.py

x = 42
def bar():
    ...

def spam():
    ...
```

`foo.__dict__` 또는 `globals()`를 검사하면 딕셔너리를 볼 수 있습니다.

```python
{
    'x' : 42,
    'bar' : <function bar>,
    'spam' : <function spam>
}
```
