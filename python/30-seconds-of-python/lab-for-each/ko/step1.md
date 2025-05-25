# 리스트 각 요소에 대해 함수 실행하기

리스트 `itr`과 함수 `fn`을 인수로 받는 함수 `for_each(itr, fn)`을 작성하십시오. 이 함수는 `itr`의 각 요소에 대해 `fn`을 한 번 실행해야 합니다.

```python
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```python
for_each([1, 2, 3], print) # 1 2 3
```
