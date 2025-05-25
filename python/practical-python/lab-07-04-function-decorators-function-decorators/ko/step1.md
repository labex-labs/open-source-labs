# 로깅 예시

함수를 생각해 봅시다.

```python
def add(x, y):
    return x + y
```

이제, 로깅 (logging) 이 추가된 함수를 생각해 봅시다.

```python
def add(x, y):
    print('Calling add')
    return x + y
```

이제 두 번째 함수도 로깅이 추가되었습니다.

```python
def sub(x, y):
    print('Calling sub')
    return x - y
```
