# 리스트를 딕셔너리로 매핑하기

`map_dictionary(itr, fn)`이라는 Python 함수를 작성하세요. 이 함수는 두 개의 매개변수를 받습니다.

- `itr`: 값의 리스트
- `fn`: 값을 입력으로 받아 값을 출력으로 반환하는 함수

이 함수는 키 - 값 쌍이 원래 값을 키로 하고 함수의 결과를 값으로 하는 딕셔너리를 반환해야 합니다.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `map()`을 사용하여 리스트의 각 값에 `fn`을 적용합니다.
2. `zip()`을 사용하여 원래 값을 `fn`에 의해 생성된 값과 쌍으로 묶습니다.
3. `dict()`를 사용하여 적절한 딕셔너리를 반환합니다.

```python
def map_dictionary(itr, fn):
  return dict(zip(itr, map(fn, itr)))
```

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```
