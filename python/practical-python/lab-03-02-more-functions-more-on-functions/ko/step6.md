# 다중 반환 값 (Multiple Return Values)

함수는 하나의 값만 반환할 수 있습니다. 하지만, 함수는 튜플 (tuple) 로 반환하여 여러 값을 반환할 수 있습니다.

```python
def divide(a,b):
    q = a // b      # 몫 (Quotient)
    r = a % b       # 나머지 (Remainder)
    return q, r     # 튜플 반환 (Return a tuple)
```

사용 예시:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
