# 딕셔너리 값

평평한 딕셔너리가 주어지면, 딕셔너리의 모든 값을 평평한 리스트로 반환하는 함수를 만들어야 합니다. `values_only(flat_dict)` 함수를 구현하는 것이 목표이며, 이 함수는 평평한 딕셔너리를 인수로 받아 딕셔너리의 모든 값을 리스트로 반환합니다.

이 문제를 해결하기 위해 `dict.values()` 메서드를 사용하여 주어진 딕셔너리의 값을 반환할 수 있습니다. 그런 다음 `list()` 함수를 사용하여 결과를 리스트로 변환할 수 있습니다.

```python
def values_only(flat_dict):
  return list(flat_dict.values())
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```
