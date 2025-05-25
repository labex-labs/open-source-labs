# 연습 문제 6.4: 간단한 제너레이터 (Generator)

반복을 사용자 정의하고 싶을 때마다 항상 제너레이터 함수를 생각해야 합니다. 작성하기 쉽습니다. 원하는 반복 로직을 수행하는 함수를 만들고 `yield`를 사용하여 값을 내보냅니다.

예를 들어, 파일에서 일치하는 부분 문자열을 포함하는 줄을 검색하는 이 제너레이터를 사용해 보세요.

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

이것은 다소 흥미롭습니다. 사용자 정의 처리를 함수에 숨기고 이를 사용하여 for 루프에 공급할 수 있다는 아이디어입니다. 다음 예제는 더 특이한 경우를 살펴봅니다.
