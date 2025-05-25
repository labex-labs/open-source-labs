# 연습 문제 3.11: 모듈 import

3 장에서 CSV 데이터 파일의 내용을 파싱하기 위한 범용 함수 `parse_csv()`를 만들었습니다.

이제 해당 함수를 다른 프로그램에서 사용하는 방법을 살펴보겠습니다. 먼저, 새 셸 창을 시작합니다. 모든 파일이 있는 폴더로 이동합니다. 파일을 import 할 것입니다.

Python 대화형 모드를 시작합니다.

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

그렇게 했다면, 이전에 작성한 프로그램 중 일부를 import 해 보세요. 이전과 정확히 동일한 출력을 볼 수 있습니다. 강조하자면, 모듈을 import 하면 해당 코드가 실행됩니다.

```python
>>> import bounce
... watch output ...
>>> import mortgage
... watch output ...
>>> import report
... watch output ...
>>>
```

이 중 어느 것도 작동하지 않으면, 아마도 잘못된 디렉토리에서 Python 을 실행하고 있을 것입니다. 이제 `fileparse` 모듈을 import 하고 이에 대한 도움말을 얻어보세요.

```python
>>> import fileparse
>>> help(fileparse)
... look at the output ...
>>> dir(fileparse)
... look at the output ...
>>>
```

모듈을 사용하여 일부 데이터를 읽어보세요:

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... look at the output ...
>>> prices = dict(pricelist)
>>> prices
... look at the output ...
>>> prices['IBM']
106.28
>>>
```

모듈 이름을 포함할 필요가 없도록 함수를 import 해 보세요:

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>>
```
