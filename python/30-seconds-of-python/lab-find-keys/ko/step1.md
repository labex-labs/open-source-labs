# 값으로 키 찾기

`find_keys(dictionary, value)`라는 파이썬 함수를 작성하세요. 이 함수는 딕셔너리와 값을 인수로 받아 주어진 값을 가진 딕셔너리의 모든 키 목록을 반환합니다. 주어진 값을 가진 키가 없으면 함수는 빈 목록을 반환해야 합니다.

이 문제를 해결하기 위해 딕셔너리의 키 - 값 쌍을 생성하는 `dictionary.items()` 메서드를 사용할 수 있습니다. 그런 다음 리스트 컴프리헨션 (list comprehension) 을 사용하여 주어진 값을 가진 키를 필터링할 수 있습니다.

```python
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```
