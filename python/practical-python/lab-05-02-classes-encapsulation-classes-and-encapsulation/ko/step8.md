# 균일한 접근 (Uniform access)

마지막 예제는 객체에 더 균일한 인터페이스를 어떻게 적용하는지 보여줍니다. 이렇게 하지 않으면 객체를 사용하는 것이 혼란스러울 수 있습니다.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> a = s.cost() # Method
49010.0
>>> b = s.shares # Data attribute
100
>>>
```

`cost`에는 `()`가 필요한데, `shares`에는 왜 필요하지 않을까요? 프로퍼티가 이를 해결할 수 있습니다.
