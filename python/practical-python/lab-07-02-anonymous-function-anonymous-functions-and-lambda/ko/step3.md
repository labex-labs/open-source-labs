# 람다: 익명 함수 (Anonymous Functions)

함수를 생성하는 대신 람다를 사용하십시오. 이전 정렬 예제에서:

```python
portfolio.sort(key=lambda s: s['name'])
```

이것은 _이름 없는_ 함수를 생성하여 _단일_ 표현식을 평가합니다. 위의 코드는 초기 코드보다 훨씬 짧습니다.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```
