# 값으로 리스트 초기화

`initialize_list_with_values(n, val=0)` 함수를 작성하세요. 이 함수는 두 개의 매개변수를 받습니다.

- `n` (정수): 생성할 리스트의 길이를 나타냅니다.
- `val` (정수): 리스트를 채우는 데 사용할 값을 나타냅니다. `val`이 제공되지 않으면 기본값 `0`을 사용해야 합니다.

이 함수는 지정된 값으로 채워진 길이가 `n`인 리스트를 반환해야 합니다.

```python
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]
```

```python
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```
