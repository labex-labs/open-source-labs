# 리스트의 고유 요소

`unique_elements`라는 Python 함수를 작성하여 리스트를 입력으로 받아 고유한 요소만 포함하는 새로운 리스트를 반환하십시오. 함수는 다음 단계를 수행해야 합니다.

- 중복된 값을 버리기 위해 리스트에서 `set`을 생성합니다.
- set 에서 `list`를 반환합니다.

함수는 다음과 같은 시그니처를 가져야 합니다.

```python
def unique_elements(li: List) -> List:
```

```python
def unique_elements(li):
  return list(set(li))
```

```python
unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]
```
