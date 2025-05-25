# 연습 문제 5.7: Property 와 Setter

`shares` 속성을 수정하여 값을 private 속성에 저장하고, property 함수 쌍을 사용하여 항상 정수 값으로 설정되도록 합니다. 예상되는 동작의 예는 다음과 같습니다.

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected an integer
>>>
```
