# 리스트 유사성

두 개의 리스트 `a`와 `b`를 인수로 받아 두 리스트 `a`와 `b` 모두에 존재하는 요소만 포함하는 새로운 리스트를 반환하는 함수 `similarity(a, b)`를 작성하십시오.

이 문제를 해결하기 위해 리스트 컴프리헨션 (list comprehension) 을 사용하여 `a`의 요소를 반복하고 해당 요소가 `b`에 존재하는지 확인할 수 있습니다. 요소가 두 리스트 모두에 존재하면 새 리스트에 추가합니다.

```python
def similarity(a, b):
  return [item for item in a if item in b]
```

```python
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```
