# 연습 문제 6.15: 코드 단순화

제너레이터 표현식은 종종 작은 제너레이터 함수를 대체하는 데 유용합니다. 예를 들어, 다음과 같은 함수를 작성하는 대신:

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

다음과 같이 작성할 수 있습니다:

```python
rows = (row for row in rows if row['name'] in names)
```

`ticker.py` 프로그램을 수정하여 적절하게 제너레이터 표현식을 사용하십시오.
