# 리스트 요소 그룹화

리스트 `lst`와 함수 `fn`을 인수로 받아, `fn`을 `lst`의 요소에 적용한 결과가 키이고, `fn`을 적용했을 때 해당 키를 생성하는 `lst`의 요소 리스트가 값인 딕셔너리를 반환하는 함수 `group_by(lst, fn)`을 작성하십시오.

예를 들어, 숫자 리스트 `[6.1, 4.2, 6.3]`이 있고, 정수 부분별로 그룹화하려는 경우, `math` 모듈의 `floor` 함수를 그룹화 함수로 사용할 수 있습니다. 예상되는 출력은 `{4: [4.2], 6: [6.1, 6.3]}`입니다.

```python
from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
