# 연습 문제 1.30: 스크립트를 함수로 변환하기 (Turning a script into a function)

연습 문제 1.27 에서 `pcost.py` 프로그램에 대해 작성한 코드를 가져와서 `portfolio_cost(filename)` 함수로 변환하십시오. 이 함수는 파일 이름을 입력으로 받아 해당 파일의 포트폴리오 데이터를 읽고 포트폴리오의 총 비용을 float 로 반환합니다.

함수를 사용하려면 프로그램을 다음과 같이 변경하십시오:

```python
# pcost.py
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
```

프로그램을 실행하면 이전과 동일한 출력을 볼 수 있습니다. 프로그램을 실행한 후에는 다음과 같이 입력하여 함수를 대화형으로 호출할 수도 있습니다:

```bash
$ python3 -i pcost.py
```

이렇게 하면 대화형 모드에서 함수를 호출할 수 있습니다.

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

코드를 대화형으로 실험할 수 있는 것은 테스트 및 디버깅에 유용합니다.
