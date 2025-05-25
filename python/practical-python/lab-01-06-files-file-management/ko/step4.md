# 연습 1.26: 파일 예비 작업 (File Preliminaries)

먼저, 전체 파일을 한 번에 큰 문자열로 읽어보세요.

```python
>>> with open('portfolio.csv', 'rt') as f:
        data = f.read()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

위의 예에서 Python 은 두 가지 출력 모드를 가지고 있다는 점에 유의해야 합니다. 프롬프트에서 `data`를 입력하는 첫 번째 모드에서는 Python 이 따옴표와 이스케이프 코드를 포함한 원시 문자열 표현을 보여줍니다. `print(data)`를 입력하면 문자열의 실제 서식 지정된 출력을 얻습니다.

파일을 한 번에 모두 읽는 것은 간단하지만, 특히 파일이 거대하거나 한 번에 처리하려는 텍스트 줄이 포함된 경우, 항상 가장 적절한 방법은 아닙니다.

파일을 줄 단위로 읽으려면 다음과 같이 for 루프를 사용하십시오.

```python
>>> with open('portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

이 코드를 표시된 대로 사용하면 파일 끝에 도달할 때까지 줄이 읽히고, 이 시점에서 루프가 중지됩니다.

특정 경우에, 텍스트의 _단일_ 줄을 수동으로 읽거나 건너뛸 수 있습니다 (예: 열 머리글의 첫 번째 줄을 건너뛰고 싶을 수 있습니다).

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()`는 파일의 다음 텍스트 줄을 반환합니다. 반복적으로 호출하면 연속적인 줄을 얻게 됩니다. 그러나 알아두어야 할 점은 `for` 루프가 이미 `next()`를 사용하여 데이터를 얻는다는 것입니다. 따라서 표시된 것처럼 명시적으로 단일 줄을 건너뛰거나 읽으려는 경우가 아니면 일반적으로 직접 호출하지 않습니다.

파일의 줄을 읽으면 분할과 같은 더 많은 처리를 시작할 수 있습니다. 예를 들어, 다음을 시도해 보십시오.

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name', 'shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
```

_참고: 이 예제에서는 `with` 문이 사용되지 않으므로 `f.close()`가 명시적으로 호출됩니다._
