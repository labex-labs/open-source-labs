# 연습 문제 2.26: 전체 그림 (The Big Picture)

이 연습 문제의 기술을 사용하여 거의 모든 열 지향 데이터 파일의 필드를 Python 딕셔너리로 쉽게 변환하는 문을 작성할 수 있습니다.

단지 예시를 위해, 다음과 같이 다른 데이터 파일에서 데이터를 읽는다고 가정해 봅시다.

```python
>>> f = open('dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

비슷한 트릭을 사용하여 필드를 변환해 봅시다.

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
```

보너스: `date` 항목을 `(6, 11, 2007)`와 같은 튜플로 추가로 구문 분석하도록 이 예제를 어떻게 수정하시겠습니까?

이 연습 문제에서 수행한 작업을 숙고하는 데 시간을 할애하십시오. 이러한 아이디어는 나중에 다시 살펴볼 것입니다.
