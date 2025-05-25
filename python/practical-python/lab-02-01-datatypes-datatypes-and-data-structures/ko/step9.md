# 일반적인 연산 (Common operations)

딕셔너리에서 값을 가져오려면 키 이름을 사용하십시오.

```python
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

값을 추가하거나 수정하려면 키 이름을 사용하여 할당하십시오.

```python
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

값을 삭제하려면 `del` 문을 사용하십시오.

```python
>>> del s['date']
>>>
```
