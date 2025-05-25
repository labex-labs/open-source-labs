# 딕셔너리 값 매핑 (Map Dictionary Values)

딕셔너리 `obj`와 함수 `fn`을 인수로 받아, 원래 딕셔너리와 동일한 키를 가지고 각 값에 대해 제공된 함수를 실행하여 생성된 값을 갖는 새로운 딕셔너리를 반환하는 함수 `map_values(obj, fn)`을 작성하십시오.

```python
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```
