# 함수를 기반으로 리스트의 최소값 찾기

`min_by(lst, fn)`이라는 함수를 작성하세요. 이 함수는 리스트 `lst`와 함수 `fn`을 인수로 받습니다. 이 함수는 제공된 함수를 사용하여 리스트의 각 요소를 값에 매핑한 다음, 최소값을 반환해야 합니다.

```python
def min_by(lst, fn):
  return min(map(fn, lst))
```

```python
min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2
```
