# 연습 문제 3.2: 프로그램 실행을 위한 최상위 함수 생성

프로그램의 마지막 부분을 가져와 단일 함수 `portfolio_report(portfolio_filename, prices_filename)`로 패키징합니다. 다음 함수 호출이 이전과 같이 보고서를 생성하도록 함수를 작동시킵니다.

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

이 최종 버전에서 프로그램은 일련의 함수 정의와 맨 마지막에 `portfolio_report()`에 대한 단일 함수 호출 (프로그램에 관련된 모든 단계를 실행) 로 구성됩니다.

프로그램을 단일 함수로 변환하면 다른 입력에 대해 쉽게 실행할 수 있습니다. 예를 들어, 프로그램을 실행한 후 다음 문을 대화형으로 시도해 보십시오.

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... look at the output ...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... look at the output ...
>>>
```
