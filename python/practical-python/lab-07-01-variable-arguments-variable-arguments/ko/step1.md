# 위치 가변 인자 (`*args`)

*임의의 수*의 인자를 허용하는 함수는 가변 인자를 사용한다고 합니다. 예를 들어 다음과 같습니다.

```python
def f(x, *args):
    ...
```

함수 호출.

```python
f(1,2,3,4,5)
```

추가 인자는 튜플로 전달됩니다.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```
