# 딕셔너리가 필요한 이유 (Why dictionaries?)

딕셔너리는 _많은_ 서로 다른 값이 있고 해당 값을 수정하거나 조작해야 할 때 유용합니다. 딕셔너리는 코드를 더 읽기 쉽게 만듭니다.

```python
s['price']
# vs
s[2]
```

지난 몇 개의 연습에서, 데이터 파일 `portfolio.csv`를 읽는 프로그램을 작성했습니다. `csv` 모듈을 사용하면 파일을 행별로 쉽게 읽을 수 있습니다.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name', 'shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

파일을 읽는 것은 쉽지만, 종종 데이터를 읽는 것 이상을 수행하고 싶을 것입니다. 예를 들어, 데이터를 저장하고 일부 계산을 수행하기 시작할 수 있습니다. 불행히도, 원시 "행" 데이터는 작업할 수 있는 충분한 정보를 제공하지 않습니다. 예를 들어, 간단한 수학 계산조차 작동하지 않습니다.

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

더 많은 작업을 수행하려면 일반적으로 원시 데이터를 어떤 방식으로 해석하고 나중에 작업할 수 있도록 더 유용한 종류의 객체로 변환해야 합니다. 두 가지 간단한 옵션은 튜플 (tuples) 또는 딕셔너리 (dictionaries) 입니다.
