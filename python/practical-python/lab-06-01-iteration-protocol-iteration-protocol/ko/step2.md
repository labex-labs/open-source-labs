# 반복: 프로토콜 (Iteration: Protocol)

`for` 문을 생각해 봅시다.

```python
for x in obj:
    # statements
```

내부적으로 무슨 일이 일어날까요?

```python
_iter = obj.__iter__()        # 이터레이터 객체 가져오기 (Get iterator object)
while True:
    try:
        x = _iter.__next__()  # 다음 항목 가져오기 (Get next item)
        # statements ...
    except StopIteration:     # 더 이상 항목 없음 (No more items)
        break
```

`for-loop`와 함께 작동하는 모든 객체는 이 하위 수준의 반복 프로토콜을 구현합니다.

예시: 리스트 수동 반복.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```
