# 둘 다 결합하기

함수는 또한 임의의 수의 가변 키워드 및 비 키워드 인자를 허용할 수 있습니다.

```python
def f(*args, **kwargs):
    ...
```

함수 호출.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

인자는 위치 인자와 키워드 구성 요소로 분리됩니다.

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    ...
```

이 함수는 위치 인자 또는 키워드 인자의 모든 조합을 받습니다. 이는 래퍼 (wrapper) 를 작성하거나 다른 함수로 인자를 전달하려는 경우에 사용됩니다.
