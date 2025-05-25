# 딕셔너리 키 (Dictionary Keys)

플랫 딕셔너리를 입력으로 받아 모든 키의 목록을 반환하는 함수 `keys_only(flat_dict)`를 작성하십시오.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `dict.keys()`를 사용하여 주어진 딕셔너리의 키를 반환합니다.
2. 이전 결과의 `list()`를 반환합니다.

```python
def keys_only(flat_dict):
  return list(flat_dict.keys())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
