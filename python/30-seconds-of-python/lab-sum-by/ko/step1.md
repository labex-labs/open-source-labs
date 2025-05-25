# 함수 기반 리스트 합계

리스트 `lst`와 함수 `fn`을 인수로 받는 함수 `sum_by(lst, fn)`을 작성하십시오. 이 함수는 제공된 함수를 사용하여 리스트의 각 요소를 값에 매핑하고, 해당 값들의 합계를 반환해야 합니다.

```python
def sum_by(lst, fn):
  return sum(map(fn, lst))
```

```python
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```
