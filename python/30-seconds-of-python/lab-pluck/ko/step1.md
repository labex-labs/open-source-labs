# 딕셔너리 목록에서 값 추출하기

딕셔너리 목록 `lst`와 키 `key`를 인수로 받아 지정된 `key`에 해당하는 값의 목록을 반환하는 함수 `pluck(lst, key)`를 작성하십시오.

다음 사항을 수행해야 합니다.

- 리스트 컴프리헨션 (list comprehension) 과 `dict.get()`을 사용하여 `lst`의 각 딕셔너리에 대한 `key`의 값을 가져옵니다.
- 입력 목록이 비어 있거나 지정된 키가 딕셔너리에 존재하지 않는 경우 함수는 빈 목록을 반환해야 합니다.

```python
def pluck(lst, key):
  return [x.get(key) for x in lst]
```

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name': 'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(simpsons, 'age') # [8, 36, 34, 10]
```
