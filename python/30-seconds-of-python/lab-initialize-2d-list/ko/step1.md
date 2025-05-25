# 2D 리스트 초기화

주어진 너비와 높이 및 값으로 2D 리스트를 초기화하는 함수 `initialize_2d_list(w, h, val=None)`을 작성하십시오. 이 함수는 `h`개의 행으로 구성된 리스트를 반환해야 하며, 각 행은 `w` 길이를 가진 리스트로, `val`로 초기화됩니다. `val`이 제공되지 않으면 기본값은 `None`이어야 합니다.

```python
def initialize_2d_list(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]
```

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
```
