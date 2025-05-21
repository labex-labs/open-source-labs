# CSV 파일에서 포트폴리오 읽기

이 단계에서는 CSV 파일에서 주식 데이터를 읽고 `Stock` 객체 목록을 반환하는 함수를 만들 것입니다. `Stock` 객체는 주식 보유를 나타내며, 이 단계를 마치면 CSV 파일에서 주식 포트폴리오를 읽을 수 있게 됩니다.

## CSV 파일 이해하기

CSV 는 쉼표로 구분된 값 (Comma-Separated Values) 의 약자로, 표 형식 데이터를 저장하는 매우 일반적인 형식입니다. 간단한 스프레드시트라고 생각하면 됩니다. CSV 파일의 각 줄은 데이터 행을 나타내고, 해당 행 내의 열은 쉼표로 구분됩니다. 일반적으로 CSV 파일의 첫 번째 줄에는 헤더가 포함되어 있습니다. 이러한 헤더는 각 열에 어떤 종류의 데이터가 있는지 설명합니다. 예를 들어, 주식 포트폴리오 CSV 에서 헤더는 "Name", "Shares", "Price"일 수 있습니다.

## 구현 지침

1. 먼저 코드 편집기에서 `stock.py` 파일을 엽니다. 이미 열려 있다면 좋습니다! 그렇지 않은 경우 파일을 찾아 엽니다. 여기에 새 함수를 추가할 것입니다.

2. `stock.py` 파일이 열리면 `# TODO: Add read_portfolio(filename) function here` 주석을 찾습니다. 이 주석은 새 함수를 넣을 위치를 알려주는 자리 표시자입니다.

3. 해당 주석 아래에 다음 함수를 추가합니다. 이 함수는 `read_portfolio`라고 하며, 파일 이름을 인수로 사용합니다. 이 함수의 목적은 CSV 파일을 읽고, 주식 데이터를 추출하고, `Stock` 객체 목록을 만드는 것입니다.

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

이 함수가 수행하는 작업을 자세히 살펴보겠습니다. 먼저 `portfolio`라는 빈 목록을 만듭니다. 그런 다음 읽기 모드로 CSV 파일을 엽니다. `next(f)` 문은 첫 번째 줄인 헤더 줄을 건너뜁니다. 그 후, 파일의 각 줄을 반복합니다. 각 줄에 대해 줄을 값 목록으로 분할하고, 이름, 주식 수 및 가격을 추출하고, `Stock` 객체를 만들고, 이를 `portfolio` 목록에 추가합니다. 마지막으로 `portfolio` 목록을 반환합니다.

4. 함수를 추가한 후 `stock.py` 파일을 저장합니다. 키보드에서 `Ctrl+S`를 누르거나 코드 편집기 메뉴에서 "파일 > 저장"을 선택하여 이 작업을 수행할 수 있습니다. 파일을 저장하면 변경 사항이 유지됩니다.

5. 이제 `read_portfolio` 함수를 테스트해야 합니다. `test_portfolio.py`라는 새 Python 스크립트를 만듭니다. 이 스크립트는 `stock.py` 파일에서 `read_portfolio` 함수를 가져오고, CSV 파일에서 포트폴리오를 읽고, 포트폴리오의 각 주식에 대한 정보를 출력합니다.

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

이 스크립트에서는 먼저 `read_portfolio` 함수를 가져옵니다. 그런 다음 파일 이름 `portfolio.csv`를 사용하여 함수를 호출하여 `Stock` 객체 목록을 가져옵니다. 그 후, 목록을 반복하고 각 주식에 대한 정보를 출력합니다. 마지막으로 포트폴리오의 총 주식 수를 출력합니다.

6. 테스트 스크립트를 실행하려면 터미널 또는 명령 프롬프트를 열고, `test_portfolio.py` 파일이 있는 디렉토리로 이동하여 다음 명령을 실행합니다.

```bash
python3 test_portfolio.py
```

모든 것이 제대로 작동하면 `portfolio.csv` 파일의 모든 주식과 이름, 주식 수 및 가격이 나열된 출력이 표시됩니다. 또한 포트폴리오의 총 주식 수도 표시됩니다.

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $70.44

Total number of stocks in portfolio: 7
```

이 출력은 `read_portfolio` 함수가 CSV 파일을 올바르게 읽고 해당 데이터에서 `Stock` 객체를 생성하고 있음을 확인합니다.
