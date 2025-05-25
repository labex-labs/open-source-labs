# 문자열 서식 지정 (String Formatting)

Python 3.6 이상에서 문자열 서식을 지정하는 한 가지 방법은 `f-string`을 사용하는 것입니다.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

`{expression:format}` 부분이 대체됩니다.

이는 `print`와 함께 일반적으로 사용됩니다.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```
