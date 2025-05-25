# 연습 문제 7.6: 람다를 사용하여 필드 정렬 (Sorting on a field with lambda)

`lambda` 표현식을 사용하여 주식 수를 기준으로 포트폴리오를 정렬해 보십시오.

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... inspect the result ...
>>>
```

각 주식의 가격에 따라 포트폴리오를 정렬해 보십시오.

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... inspect the result ...
>>>
```

참고: `lambda`는 별도의 함수를 먼저 정의할 필요 없이 `sort()` 호출에서 특수한 처리 함수를 직접 정의할 수 있게 해주므로 유용한 단축키입니다.
