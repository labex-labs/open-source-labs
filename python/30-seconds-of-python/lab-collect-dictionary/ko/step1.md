# 딕셔너리 반전

입력으로 딕셔너리 `obj`를 받아 키와 값을 반전시킨 새로운 딕셔너리를 반환하는 함수 `invert_dictionary(obj)`를 작성하십시오. 입력 딕셔너리는 고유하지 않은 해시 가능한 (hashable) 값을 가집니다. 두 개 이상의 키가 동일한 값을 갖는 경우, 함수는 출력 딕셔너리의 리스트에 키를 추가해야 합니다.

이 문제를 해결하기 위해 다음 단계를 따를 수 있습니다.

1. 각 키에 대한 기본값으로 `list`를 사용하는 `collections.defaultdict`를 생성합니다.
2. `dictionary.items()`를 루프와 함께 사용하여 딕셔너리의 값을 `dict.append()`를 사용하여 키에 매핑합니다.
3. `dict()`를 사용하여 `collections.defaultdict`를 일반 딕셔너리로 변환합니다.

함수 시그니처: `def invert_dictionary(obj: dict) -> dict:`

```python
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
