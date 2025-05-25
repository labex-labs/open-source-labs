# 함수 기반 최대 리스트 값 찾기

리스트 `lst`와 함수 `fn`을 인수로 받는 함수 `max_by(lst, fn)`을 작성하십시오. 이 함수는 `lst`의 각 요소를 제공된 함수 `fn`을 사용하여 값에 매핑한 다음, 최대값을 반환해야 합니다.

```python
def max_by(lst, fn):
  return max(map(fn, lst))
```

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```
