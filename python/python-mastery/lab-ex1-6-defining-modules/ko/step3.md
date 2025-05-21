# 자신만의 모듈 만들기

이제 기존 모듈을 사용하는 방법을 이해했으므로 처음부터 새 모듈을 만들 차례입니다. Python 의 모듈은 Python 정의와 문을 포함하는 파일입니다. 코드를 재사용 가능하고 관리 가능한 조각으로 구성할 수 있습니다. 자신만의 모듈을 만들면 관련 함수와 변수를 함께 그룹화하여 코드를 더 모듈화하고 유지 관리를 쉽게 할 수 있습니다.

## 보고서 모듈 만들기

주식 보고서를 생성하기 위한 간단한 모듈을 만들어 보겠습니다. 이 모듈에는 포트폴리오 파일을 읽고 포트폴리오의 주식에 대한 형식이 지정된 보고서를 인쇄하는 함수가 있습니다.

1. 먼저, `report.py`라는 새 파일을 만들어야 합니다. 이를 위해 명령줄을 사용합니다. 홈 디렉토리의 `project` 디렉토리로 이동하여 `touch` 명령을 사용하여 파일을 만듭니다.

```bash
cd ~/project
touch report.py
```

2. 이제 선호하는 텍스트 편집기에서 `report.py` 파일을 열고 다음 코드를 추가합니다. 이 코드는 두 개의 함수와 메인 블록을 정의합니다.

```python
# report.py

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with
    keys: name, shares, price
    """
    portfolio = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                stock = {
                    'name': fields[0],
                    'shares': int(fields[1]),
                    'price': float(fields[2])
                }
                portfolio.append(stock)
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")
    return portfolio

def print_report(portfolio):
    """
    Print a report showing the stock name, shares, price, and total value
    """
    print("Name    Shares    Price    Value")
    print("-" * 40)
    total_value = 0.0
    for stock in portfolio:
        value = stock['shares'] * stock['price']
        total_value += value
        print(f"{stock['name']:6s} {stock['shares']:9d} {stock['price']:9.2f} {value:9.2f}")
    print("-" * 40)
    print(f"Total Value: {total_value:16.2f}")

if __name__ == "__main__":
    portfolio = read_portfolio('portfolio.dat')
    print_report(portfolio)
```

`read_portfolio` 함수는 주식 정보를 포함하는 파일을 읽고 각 딕셔너리가 `name`, `shares`, `price` 키가 있는 주식을 나타내는 딕셔너리 목록을 반환합니다. `print_report` 함수는 포트폴리오 (주식 딕셔너리 목록) 를 가져와 주식 이름, 주식 수, 가격 및 총 가치를 표시하는 형식이 지정된 보고서를 인쇄합니다. 마지막의 메인 블록은 파일이 직접 실행될 때 실행됩니다. 포트폴리오 파일을 읽고 보고서를 인쇄합니다.

3. 코드를 추가한 후 저장하고 편집기를 종료합니다.

## 모듈 테스트하기

새 모듈이 예상대로 작동하는지 확인하기 위해 테스트해 보겠습니다.

1. 먼저, 명령줄에서 스크립트를 직접 실행합니다. 이렇게 하면 `report.py` 파일의 메인 블록이 실행됩니다.

```bash
python3 report.py
```

포트폴리오 주식과 해당 가치를 보여주는 형식이 지정된 보고서가 표시됩니다. 이 보고서에는 주식 이름, 주식 수, 가격 및 총 가치와 전체 포트폴리오의 총 가치가 포함됩니다.

```
Name    Shares    Price    Value
----------------------------------------
AA         100     32.20   3220.00
IBM         50     91.10   4555.00
CAT        150     83.44  12516.00
MSFT       200     51.23  10246.00
GE          95     40.37   3835.15
MSFT        50     65.10   3255.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         44671.15
```

2. 다음으로, Python 인터프리터에서 모듈을 사용합니다. 터미널에서 `python3` 명령을 실행하여 Python 인터프리터를 시작합니다.

```bash
python3
```

인터프리터가 실행되면 `report` 모듈을 가져와 해당 함수를 사용할 수 있습니다.

```python
import report
portfolio = report.read_portfolio('portfolio.dat')
len(portfolio)  # Should return 7, the number of stocks
portfolio[0]    # First stock in the portfolio
```

`import report` 문은 `report.py` 파일에 정의된 함수와 변수를 현재 Python 세션에서 사용할 수 있도록 합니다. 그런 다음 `read_portfolio` 함수를 사용하여 포트폴리오 파일을 읽고 결과를 `portfolio` 변수에 저장합니다. `len(portfolio)` 문은 포트폴리오의 주식 수를 반환하고 `portfolio[0]`은 포트폴리오의 첫 번째 주식을 반환합니다.

다음 출력이 표시됩니다.

```
7
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

3. 이제 가져온 모듈을 사용하여 포트폴리오의 총 비용을 직접 계산해 보겠습니다. 포트폴리오의 주식을 반복하고 각 주식의 총 가치를 합산합니다.

```python
total = 0.0
for stock in portfolio:
    total += stock['shares'] * stock['price']
print(total)
```

출력은 `44671.15`여야 하며, 이는 `print_report` 함수에서 인쇄된 총 가치와 동일합니다.

4. 마지막으로, 특정 주식 유형에 대한 사용자 지정 보고서를 만들어 보겠습니다. 포트폴리오를 필터링하여 IBM 주식만 포함한 다음 `print_report` 함수를 사용하여 해당 주식에 대한 보고서를 인쇄합니다.

```python
ibm_stocks = [stock for stock in portfolio if stock['name'] == 'IBM']
report.print_report(ibm_stocks)
```

이렇게 하면 IBM 주식과 해당 가치만 표시하는 보고서가 인쇄됩니다.

```
Name    Shares    Price    Value
----------------------------------------
IBM         50     91.10   4555.00
IBM        100     70.44   7044.00
----------------------------------------
Total Value:         11599.00
```

5. 테스트를 마쳤으면 `exit()` 명령을 실행하여 Python 인터프리터를 종료합니다.

```python
exit()
```

이제 자신만의 Python 모듈을 성공적으로 만들고 사용했으며, 함수와 파일이 직접 실행될 때만 실행되는 메인 블록을 모두 결합했습니다. 이 모듈식 프로그래밍 방식은 코드를 재사용하고 프로젝트를 더 체계적으로 유지 관리할 수 있도록 합니다.
