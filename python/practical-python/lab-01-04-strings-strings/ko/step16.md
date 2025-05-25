# 연습 1.17: f-문자열 (f-strings)

때로는 문자열을 생성하고 변수의 값을 문자열에 포함시키고 싶을 때가 있습니다.

그렇게 하려면 f-문자열을 사용하십시오. 예를 들어:

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>>
```

연습 1.10 의 `mortgage.py` 프로그램을 수정하여 f-문자열을 사용하여 출력을 생성하십시오. 출력이 보기 좋게 정렬되도록 시도하십시오.
