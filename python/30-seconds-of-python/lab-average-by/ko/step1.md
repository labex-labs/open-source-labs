# 매핑된 리스트 평균

`average_by(lst, fn = lambda x: x)`라는 함수를 작성하세요. 이 함수는 리스트 `lst`와 함수 `fn`을 인수로 받습니다. 함수 `fn`은 리스트의 각 요소를 값에 매핑하는 데 사용해야 합니다. 그런 다음 함수는 매핑된 값의 평균을 계산하여 반환해야 합니다.

`fn` 인수가 제공되지 않으면 함수는 요소 자체를 단순히 반환하는 기본 항등 함수를 사용해야 합니다.

작성하는 함수는 다음 요구 사항을 충족해야 합니다.

- `map()`을 사용하여 각 요소를 `fn`에서 반환된 값에 매핑합니다.
- `sum()`을 사용하여 매핑된 모든 값을 더하고, `len(lst)`로 나눕니다.
- 기본 항등 함수를 사용하기 위해 마지막 인수 `fn`을 생략합니다.

함수 시그니처: `def average_by(lst, fn = lambda x: x) -> float:`

```python
def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
```

```python
average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])
# 5.0
```
