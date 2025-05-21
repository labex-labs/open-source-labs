# 함수 정의하기

이 단계에서는 함수를 만드는 방법을 배우겠습니다. Python 에서 함수는 단일 관련 작업을 수행하는 데 사용되는, 구성되고 재사용 가능한 코드 블록입니다. 여기서는 함수가 파일에서 포트폴리오 데이터를 읽고 총 비용을 계산합니다. 이 함수가 있으면 다양한 포트폴리오 파일에 대해 여러 번 사용할 수 있으므로 동일한 코드를 반복해서 작성할 필요가 없으므로 유용합니다.

## 문제 이해하기

이전 랩에서 포트폴리오 데이터를 읽고 총 비용을 계산하는 코드를 작성했을 수 있습니다. 그러나 해당 코드는 쉽게 재사용할 수 없는 방식으로 작성되었을 것입니다. 이제 해당 코드를 재사용 가능한 함수로 변환할 것입니다.

포트폴리오 데이터 파일은 특정 형식을 가지고 있습니다. "Symbol Shares Price" 형식으로 정보를 포함합니다. 파일의 각 줄은 주식 보유를 나타냅니다. 예를 들어, `portfolio.dat`라는 파일에서 다음과 같은 줄을 볼 수 있습니다.

```
AA 100 32.20
IBM 50 91.10
...
```

여기서 첫 번째 부분 ("AA" 또는 "IBM"과 같은) 은 주식 기호 (stock symbol) 이며, 주식의 고유 식별자입니다. 두 번째 부분은 해당 주식의 보유 주식 수이고, 세 번째 부분은 주당 가격입니다.

## 함수 만들기

`/home/labex/project` 디렉토리에 `pcost.py`라는 Python 파일을 만들어 보겠습니다. 이 파일에는 함수가 포함됩니다. 다음은 `pcost.py` 파일에 넣을 코드입니다.

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file

    Args:
        filename: The name of the portfolio file

    Returns:
        The total cost of the portfolio as a float
    """
    total_cost = 0.0

    # Open the file and read through each line
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            # Extract the data (symbol, shares, price)
            shares = int(fields[1])
            price = float(fields[2])
            # Add the cost to our running total
            total_cost += shares * price

    return total_cost

# Call the function with the portfolio.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

이 코드에서 먼저 `filename`을 인수로 사용하는 `portfolio_cost`라는 함수를 정의합니다. 함수 내부에서 `total_cost` 변수를 0.0 으로 초기화합니다. 그런 다음 읽기 모드 (`'r'`) 로 `open` 함수를 사용하여 파일을 엽니다. `for` 루프를 사용하여 파일의 각 줄을 반복합니다. 각 줄에 대해 `split()` 메서드를 사용하여 필드로 분할합니다. 그런 다음 주식 수를 추출하여 정수로 변환하고 가격을 추출하여 부동 소수점으로 변환합니다. 주식 수에 가격을 곱하여 해당 주식 보유에 대한 비용을 계산하고 이를 `total_cost`에 추가합니다. 마지막으로 `total_cost`를 반환합니다.

`if __name__ == '__main__':` 부분은 스크립트가 직접 실행될 때 함수를 호출하는 데 사용됩니다. `portfolio.dat` 파일의 경로를 함수에 전달하고 결과를 출력합니다.

## 함수 테스트하기

이제 프로그램이 제대로 작동하는지 확인하기 위해 실행해 보겠습니다. `pcost.py` 파일이 있는 디렉토리로 이동한 다음 Python 스크립트를 실행해야 합니다. 다음은 그렇게 하기 위한 명령입니다.

```bash
cd /home/labex/project
python3 pcost.py
```

이러한 명령을 실행하면 다음 출력이 표시됩니다.

```
44671.15
```

이 출력은 포트폴리오의 모든 주식의 총 비용을 나타냅니다.

## 코드 이해하기

함수가 수행하는 작업을 단계별로 살펴보겠습니다.

1.  `filename`을 입력 매개변수로 사용합니다. 이를 통해 다른 포트폴리오 파일로 함수를 사용할 수 있습니다.
2.  파일을 열고 줄 단위로 읽습니다. 이는 `open` 함수와 `for` 루프를 사용하여 수행됩니다.
3.  각 줄에 대해 `split()` 메서드를 사용하여 줄을 필드로 분할합니다. 이 메서드는 공백을 기준으로 줄을 문자열 목록으로 분할합니다.
4.  주식 수를 정수로 변환하고 가격을 부동 소수점으로 변환합니다. 파일에서 읽은 데이터가 문자열 형식이고 산술 연산을 수행해야 하므로 필요합니다.
5.  각 주식 보유에 대한 비용 (주식 \* 가격) 을 계산하고 이를 실행 중인 총계에 추가합니다. 이렇게 하면 포트폴리오의 총 비용이 계산됩니다.
6.  최종 총 비용을 반환합니다. 이를 통해 필요한 경우 프로그램의 다른 부분에서 결과를 사용할 수 있습니다.

이 함수는 이제 재사용 가능합니다. 다른 포트폴리오 파일로 호출하여 비용을 계산할 수 있으므로 코드를 더 효율적으로 유지 관리할 수 있습니다.
