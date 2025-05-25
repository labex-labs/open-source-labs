# 복합 키 (Composite keys)

Python 에서는 거의 모든 유형의 값을 딕셔너리 키로 사용할 수 있습니다. 딕셔너리 키는 불변 (immutable) 타입이어야 합니다. 예를 들어, 튜플 (tuple) 과 같습니다.

```python
holidays = {
  (1, 1) : 'New Years',
  (3, 14) : 'Pi day',
  (9, 13) : "Programmer's day",
}
```

접근 방법:

```python
>>> holidays[3, 14]
'Pi day'
>>>
```

_리스트 (list), 세트 (set), 또는 다른 딕셔너리는 딕셔너리 키로 사용할 수 없습니다. 리스트와 딕셔너리는 가변 (mutable) 이기 때문입니다._
