# 연습 문제 7.5: 필드 정렬 (Sorting on a field)

다음 문을 시도하여 포트폴리오 데이터를 주식 이름순으로 알파벳순으로 정렬하십시오.

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... inspect the result ...
>>>
```

이 부분에서 `stock_name()` 함수는 `portfolio` 목록의 단일 항목에서 주식의 이름을 추출합니다. `sort()`는 이 함수의 결과를 사용하여 비교를 수행합니다.
