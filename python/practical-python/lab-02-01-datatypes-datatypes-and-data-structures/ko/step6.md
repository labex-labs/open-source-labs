# 튜플 언패킹 (Tuple Unpacking)

튜플을 다른 곳에서 사용하려면, 튜플의 부분을 변수로 언패킹 (unpacking) 할 수 있습니다.

```python
name, shares, price = s
print('Cost', shares * price)
```

왼쪽에 있는 변수의 수는 튜플 구조와 일치해야 합니다.

```python
name, shares = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
