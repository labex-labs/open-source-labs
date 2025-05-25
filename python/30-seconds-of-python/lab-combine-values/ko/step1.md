# 딕셔너리 값 결합

두 개 이상의 딕셔너리를 인수로 받아 입력 딕셔너리의 값을 결합한 새로운 딕셔너리를 반환하는 함수 `combine_values(*dicts)`를 작성하십시오. 이 함수는 다음 단계를 수행해야 합니다.

1. 각 키에 대한 기본값으로 `list`를 사용하는 새로운 `collections.defaultdict`를 생성합니다.
2. 입력 딕셔너리를 반복하고 각 딕셔너리에 대해 다음을 수행합니다.
   - 딕셔너리의 키를 반복합니다.
   - 해당 키의 값 목록에 해당 키의 값을 `defaultdict`에 추가합니다.
3. `dict()` 함수를 사용하여 `defaultdict`를 일반 딕셔너리로 변환합니다.
4. 결과 딕셔너리를 반환합니다.

함수는 다음과 같은 시그니처를 가져야 합니다.

```python
def combine_values(*dicts):
    pass
```

```python
from collections import defaultdict

def combine_values(*dicts):
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)
```

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```
