# 연습 문제 2.24: 일급 데이터 (First-class Data)

`portfolio.csv` 파일에서 다음과 같은 열로 구성된 데이터를 읽습니다.

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

이전 코드에서는 `csv` 모듈을 사용하여 파일을 읽었지만, 여전히 수동적인 타입 변환을 수행해야 했습니다. 예를 들어:

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

이러한 종류의 변환은 몇 가지 리스트 기본 연산을 사용하여 더 영리하게 수행할 수도 있습니다.

각 열을 적절한 타입으로 변환하는 데 사용할 변환 함수의 이름을 포함하는 Python 리스트를 만드십시오.

```python
>>> types = [str, int, float]
>>>
```

이 리스트를 생성할 수 있는 이유는 Python 의 모든 것이 _일급 (first-class)_ 이기 때문입니다. 따라서 함수 리스트를 원한다면 괜찮습니다. 생성한 리스트의 항목은 값 `x`를 주어진 타입으로 변환하는 함수입니다 (예: `str(x)`, `int(x)`, `float(x)`).

이제 위 파일에서 데이터 행을 읽어보세요.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

알려진 바와 같이, 이 행은 타입이 잘못되어 계산을 수행하기에 충분하지 않습니다. 예를 들어:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

그러나 데이터는 `types`에 지정한 타입과 짝을 이룰 수 있습니다. 예를 들어:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

값 중 하나를 변환해 보세요.

```python
>>> types[1](row[1])     # Same as int(row[1])
100
>>>
```

다른 값을 변환해 보세요.

```python
>>> types[2](row[2])     # Same as float(row[2])
32.2
>>>
```

변환된 값으로 계산을 시도해 보세요.

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

열 타입을 필드와 함께 zip 하고 결과를 살펴보세요.

```python
>>> r = list(zip(types, row))
>>> r
[(<type 'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

이것이 타입 변환과 값을 짝지었다는 것을 알 수 있습니다. 예를 들어, `int`는 값 `'100'`과 짝을 이룹니다.

zip 된 리스트는 모든 값에 대해 하나씩 변환을 수행하려는 경우 유용합니다. 다음을 시도해 보세요.

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

위 코드에서 무슨 일이 일어나고 있는지 이해했는지 확인하십시오. 루프에서 `func` 변수는 타입 변환 함수 중 하나입니다 (예: `str`, `int` 등) 그리고 `val` 변수는 `'AA'`, `'100'`과 같은 값 중 하나입니다. 표현식 `func(val)`은 값을 변환합니다 (일종의 타입 캐스트).

위 코드는 단일 리스트 컴프리헨션으로 압축할 수 있습니다.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
