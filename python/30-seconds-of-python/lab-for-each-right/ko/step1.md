# 각 리스트 요소에 대해 함수를 역순으로 실행

리스트 `itr`과 함수 `fn`을 인수로 받는 함수 `for_each_right(itr, fn)`을 작성하십시오. 이 함수는 `itr`의 각 요소에 대해 `fn`을 한 번씩, 마지막 요소부터 시작하여 실행해야 합니다.

```python
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```python
for_each_right([1, 2, 3], print) # 3 2 1
```
