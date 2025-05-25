# 딕셔너리 병합

두 개 이상의 딕셔너리를 인수로 받아, 입력 딕셔너리의 모든 키 - 값 쌍을 포함하는 새로운 딕셔너리를 반환하는 함수 `merge_dictionaries(*dicts)`를 작성하십시오.

함수는 새로운 딕셔너리를 생성하고 입력 딕셔너리를 반복하면서 `dictionary.update()`를 사용하여 각 딕셔너리의 키 - 값 쌍을 결과에 추가해야 합니다.

```python
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
