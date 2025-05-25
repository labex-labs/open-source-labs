# 리스트로 캐스팅 (Cast to List)

`cast_list(val)` 함수를 작성하세요. 이 함수는 값을 인수로 받아 리스트로 반환합니다. 값이 이미 리스트인 경우, 그대로 반환합니다. 값이 리스트는 아니지만 iterable(반복 가능한 객체) 인 경우, 리스트로 변환하여 반환합니다. 값이 iterable 이 아닌 경우, 단일 항목 리스트로 반환합니다.

```python
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
