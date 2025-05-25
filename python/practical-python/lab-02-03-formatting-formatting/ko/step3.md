# 딕셔너리 서식 지정 (Dictionary Formatting)

`format_map()` 메서드를 사용하여 값의 딕셔너리에 문자열 서식을 적용할 수 있습니다.

```python
>>> s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

`f-string`과 동일한 코드를 사용하지만, 제공된 딕셔너리에서 값을 가져옵니다.
