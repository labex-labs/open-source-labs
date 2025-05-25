# 최소 요소의 인덱스

정수 리스트 `arr`을 인수로 받아 리스트에서 최소값을 가진 요소의 인덱스를 반환하는 함수 `min_element_index(arr)`를 작성하세요.

이 문제를 해결하기 위해 `min()` 함수를 사용하여 리스트에서 최소값을 얻은 다음, `list.index()` 메서드를 사용하여 해당 인덱스를 반환할 수 있습니다.

```python
def min_element_index(arr):
  return arr.index(min(arr))
```

```python
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```
