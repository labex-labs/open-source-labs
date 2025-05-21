# 포트폴리오 데이터 형식 지정 및 출력

이 단계에서는 포트폴리오 데이터를 잘 정리된 표로 표시하는 데 도움이 되는 함수를 만들 것입니다. 포트폴리오는 주식의 모음이며, 이 데이터를 명확하고 읽기 쉬운 방식으로 표시하는 것이 중요합니다. 여기서 `print_portfolio(portfolio)` 함수가 등장합니다. 이 함수는 포트폴리오를 입력으로 받아 헤더와 적절한 정렬을 사용하여 표로 표시합니다.

## Python 의 문자열 형식 지정

Python 에는 문자열을 형식 지정하는 여러 가지 방법이 있습니다. 문자열 형식 지정은 데이터를 보다 체계적이고 사용자 친화적인 방식으로 표시할 수 있으므로 중요한 기술입니다.

- `%` 연산자는 이전 스타일의 문자열 형식 지정입니다. 문자열의 특정 위치에 값을 삽입할 수 있는 템플릿과 같습니다.
- `str.format()` 메서드는 또 다른 방법입니다. 문자열 형식 지정을 위한 더 많은 유연성과 더 깨끗한 구문을 제공합니다.
- f-string 은 Python 3.6 이상에서 도입된 기능입니다. 문자열 리터럴 내에 표현식을 포함할 수 있으므로 매우 편리합니다.

이 연습에서는 `%` 연산자를 사용합니다. 고정 폭 열을 만들려는 경우 특히 유용하며, 이는 포트폴리오 표에 필요한 것입니다.

## 구현 지침

1. 먼저 편집기에서 `stock.py` 파일을 엽니다. 이미 열려 있다면 좋습니다. 이 파일은 `print_portfolio` 함수를 작성할 위치입니다.

2. 파일이 열리면 `# TODO: Add print_portfolio(portfolio) function here` 주석을 찾습니다. 이 주석은 새 함수를 추가할 위치를 알려주는 마커입니다.

3. 해당 주석 아래에 다음 함수를 추가합니다.

```python
def print_portfolio(portfolio):
    """
    Print the portfolio data in a nicely formatted table.

    Args:
        portfolio (list): A list of Stock objects
    """
    # Print the header row
    print('%10s %10s %10s' % ('name', 'shares', 'price'))

    # Print a separator line
    print('-' * 10 + ' ' + '-' * 10 + ' ' + '-' * 10)

    # Print each stock in the portfolio
    for stock in portfolio:
        print('%10s %10d %10.2f' % (stock.name, stock.shares, stock.price))
```

이 함수는 먼저 표의 헤더 행을 출력한 다음 구분선과 마지막으로 포트폴리오의 각 주식을 반복하여 세부 정보를 형식 지정된 방식으로 출력합니다.

4. 함수를 추가한 후 파일을 저장합니다. `Ctrl+S`를 누르거나 메뉴에서 "파일 > 저장"을 선택하여 이 작업을 수행할 수 있습니다. 파일을 저장하면 변경 사항이 유지됩니다.

5. 이제 함수를 테스트해야 합니다. `test_print.py`라는 새 파일을 만듭니다. 이 파일은 테스트 스크립트가 됩니다. 다음 코드를 추가합니다.

```python
# test_print.py
from stock import read_portfolio, print_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a formatted table
print_portfolio(portfolio)
```

이 스크립트는 `stock.py` 파일에서 `read_portfolio` 및 `print_portfolio` 함수를 가져옵니다. 그런 다음 CSV 파일에서 포트폴리오 데이터를 읽고 새로 생성된 `print_portfolio` 함수를 사용하여 표시합니다.

6. 마지막으로 테스트 스크립트를 실행합니다. 터미널을 열고 다음 명령을 입력합니다.

```bash
python3 test_print.py
```

모든 것이 제대로 작동하면 다음과 같은 출력이 표시됩니다.

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

이 출력은 `print_portfolio` 함수가 예상대로 작동함을 확인합니다. 헤더와 정렬된 열이 있는 표로 포트폴리오 데이터를 형식 지정하고 표시하여 읽기 쉽게 만듭니다.

## 문자열 형식 지정 이해하기

`print_portfolio` 함수에서 문자열 형식 지정이 어떻게 작동하는지 자세히 살펴보겠습니다.

- `%10s`는 문자열의 형식을 지정하는 데 사용됩니다. `10`은 필드의 너비를 나타내고 `s`는 문자열을 나타냅니다. 너비가 10 인 필드 내에서 문자열을 오른쪽으로 정렬합니다.
- `%10d`는 정수를 형식 지정하는 데 사용됩니다. `10`은 필드 너비이고 `d`는 정수를 나타냅니다. 또한 너비가 10 인 필드에서 정수를 오른쪽으로 정렬합니다.
- `%10.2f`는 부동 소수점 숫자의 형식을 지정하는 데 사용됩니다. `10`은 필드 너비이고 `.2`는 부동 소수점 숫자를 소수점 2 자리까지 표시하려는 것을 지정합니다. 너비가 10 인 필드에서 부동 소수점 숫자를 오른쪽으로 정렬합니다.

이 형식 지정은 표의 모든 열이 제대로 정렬되도록 하여 출력을 훨씬 더 쉽게 읽고 이해할 수 있도록 합니다.
