# 사전 뒤집기

`invert_dictionary(obj)`라는 Python 함수를 작성하세요. 이 함수는 사전 `obj`를 인수로 받아 키와 값을 뒤집은 새로운 사전을 반환합니다. 입력 사전 `obj`는 고유하고 해시 가능한 (hashable) 값을 갖습니다. 출력 사전은 입력 사전과 동일한 키를 가져야 하지만, 값은 입력 사전의 키여야 합니다.

새로운 사전을 생성하기 위해 `dictionary.items()`를 리스트 컴프리헨션 (list comprehension) 과 함께 사용해야 합니다.

```python
def invert_dictionary(obj):
  return { value: key for key, value in obj.items() }
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```
