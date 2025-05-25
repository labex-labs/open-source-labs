# 키워드 가변 인자 (`**kwargs`)

함수는 또한 임의의 수의 키워드 인자를 허용할 수 있습니다. 예를 들어 다음과 같습니다.

```python
def f(x, y, **kwargs):
    ...
```

함수 호출.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

추가 키워드는 딕셔너리로 전달됩니다.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
```
