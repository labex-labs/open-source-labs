# 중첩 값 가져오기

딕셔너리 또는 리스트 `d`와 선택자 리스트 `selectors`를 인수로 받아 주어진 선택자 리스트에 의해 표시된 중첩 키의 값을 반환하는 함수 `get(d, selectors)`를 작성하십시오. 키가 존재하지 않으면 `None`을 반환합니다.

이 함수를 구현하기 위해 `functools.reduce()`를 사용하여 `selectors` 리스트를 반복합니다. `selectors`의 각 키에 대해 `operator.getitem()`을 적용하여 다음 반복에 대한 반복자로 사용될 값을 가져옵니다.

```python
from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
```

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```
