# 데이터 처리

이제 파일을 읽는 방법을 배웠으므로 다음 단계는 파일의 각 줄을 처리하여 각 주식 구매 비용을 계산하는 것입니다. 이는 Python 에서 데이터를 처리하는 데 중요한 부분이며, 파일을 통해 의미 있는 정보를 추출할 수 있습니다.

파일의 각 줄은 특정 형식을 따릅니다: `[주식 기호] [주식 수] [주당 가격]`. 각 주식 구매 비용을 계산하려면 각 줄에서 주식 수와 주당 가격을 추출해야 합니다. 그런 다음, 이 두 값을 곱하여 해당 특정 주식 구매 비용을 구합니다. 마지막으로, 이 비용을 총계에 더하여 포트폴리오의 전체 비용을 구합니다.

`pcost.py` 파일에서 `portfolio_cost()` 함수를 수정하여 이를 수행해 보겠습니다. 수정된 코드는 다음과 같습니다.

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split the line into fields
            fields = line.split()

            # Extract the relevant data
            # fields[0] is the stock symbol (which we don't need for the calculation)
            shares = int(fields[1])  # Number of shares (second field)
            price = float(fields[2])  # Price per share (third field)

            # Calculate the cost of this stock purchase
            cost = shares * price

            # Add to the total cost
            total_cost += cost

            # Print some debug information
            print(f'{fields[0]}: {shares} shares at ${price:.2f} = ${cost:.2f}')

    # Return the total cost
    return total_cost
```

수정된 이 함수가 수행하는 작업을 단계별로 살펴보겠습니다.

1.  **공백 제거**: `strip()` 메서드를 사용하여 각 줄의 앞뒤 공백을 제거합니다. 이렇게 하면 줄을 필드로 분할할 때 실수로 추가 공백이 포함되지 않도록 합니다.
2.  **빈 줄 건너뛰기**: 줄이 비어 있으면 (즉, 공백만 포함하는 경우) `continue` 문을 사용하여 건너뜁니다. 이렇게 하면 빈 줄을 분할하려고 할 때 오류를 방지하는 데 도움이 됩니다.
3.  **줄을 필드로 분할**: `split()` 메서드를 사용하여 각 줄을 공백을 기준으로 필드 목록으로 분할합니다. 이를 통해 줄의 각 부분에 개별적으로 액세스할 수 있습니다.
4.  **관련 데이터 추출**: 필드 목록에서 주식 수와 주당 가격을 추출합니다. 주식 수는 두 번째 필드이고, 주당 가격은 세 번째 필드입니다. 이러한 값을 적절한 데이터 유형 (`int` for shares, `float` for price) 으로 변환하여 산술 연산을 수행할 수 있도록 합니다.
5.  **비용 계산**: 주식 수에 주당 가격을 곱하여 이 주식 구매 비용을 계산합니다.
6.  **총계에 추가**: 이 주식 구매 비용을 총계에 더합니다.
7.  **디버그 정보 출력**: 각 주식 구매에 대한 일부 정보를 출력하여 어떤 일이 일어나고 있는지 확인하는 데 도움을 줍니다. 여기에는 주식 기호, 주식 수, 주당 가격 및 구매 총 비용이 포함됩니다.

이제 코드를 실행하여 작동하는지 확인해 보겠습니다. 터미널을 열고 다음 명령을 실행합니다.

```bash
python3 ~/project/pcost.py
```

명령을 실행하면 각 주식 구매에 대한 자세한 정보와 포트폴리오의 총 비용이 표시됩니다. 이 출력은 함수가 올바르게 작동하고 총 비용을 정확하게 계산했는지 확인하는 데 도움이 됩니다.
