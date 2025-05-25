# 딕셔너리에 키가 존재하는지 확인하기

딕셔너리 `d`와 키 `key`를 인수로 받아 키가 딕셔너리에 존재하면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `key_in_dict(d, key)`를 작성하십시오.

```python
def key_in_dict(d, key):
  return (key in d)
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
