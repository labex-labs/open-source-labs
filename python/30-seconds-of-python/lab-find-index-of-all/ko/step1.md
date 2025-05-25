# 모든 일치하는 인덱스 찾기

리스트 `lst`와 테스트 함수 `fn`을 인수로 받아 `lst` 내에서 `fn`이 `True`를 반환하는 모든 요소의 인덱스 목록을 반환하는 함수 `find_index_of_all(lst, fn)`을 작성하십시오.

### 입력

- 정수 리스트 `lst`.
- 정수를 입력으로 받아 부울 값을 반환하는 테스트 함수 `fn`.

### 출력

- `fn`이 `True`를 반환하는 `lst` 내 모든 요소의 인덱스를 나타내는 정수 리스트.

```python
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```python
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
