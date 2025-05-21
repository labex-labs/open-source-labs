# 파일 열기 및 읽기

이 단계에서는 Python 에서 파일을 열고 읽는 방법을 배우겠습니다. 파일 입출력 (I/O) 은 프로그래밍의 기본적인 개념입니다. 이를 통해 프로그램이 텍스트 파일, CSV 파일 등과 같은 외부 파일과 상호 작용할 수 있습니다. Python 에서 파일을 사용하는 가장 일반적인 방법 중 하나는 `open()` 함수를 사용하는 것입니다.

`open()` 함수는 Python 에서 파일을 여는 데 사용됩니다. 두 개의 중요한 인수를 받습니다. 첫 번째 인수는 열려는 파일의 이름입니다. 두 번째 인수는 파일을 열려는 모드입니다. 파일을 읽으려면 'r' 모드를 사용합니다. 이렇게 하면 Python 에 파일의 내용만 읽고 변경하지 않도록 지시합니다.

이제 `pcost.py` 파일에 `portfolio.dat` 파일을 열고 읽는 코드를 추가해 보겠습니다. 코드 편집기에서 `pcost.py` 파일을 열고 다음 코드를 추가합니다.

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            print(line)  # Just for debugging, to see what we're reading

    # Return the total cost
    return total_cost

# Call the function with the portfolio file
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

이 코드가 수행하는 작업을 자세히 살펴보겠습니다.

1. 먼저, `portfolio_cost()`라는 함수를 정의합니다. 이 함수는 파일 이름을 입력 매개변수로 받습니다. 이 함수의 목적은 파일의 데이터를 기반으로 주식 포트폴리오의 총 비용을 계산하는 것입니다.
2. 함수 내부에서 `open()` 함수를 사용하여 지정된 파일을 읽기 모드로 엽니다. `with` 문은 파일을 읽은 후 제대로 닫히도록 하는 데 사용됩니다. 이는 리소스 누수를 방지하기 위한 좋은 방법입니다.
3. 그런 다음 `for` 루프를 사용하여 파일을 줄 단위로 읽습니다. 파일의 각 줄에 대해 이를 출력합니다. 이는 디버깅 목적으로만 사용되며, 파일에서 어떤 데이터를 읽고 있는지 확인할 수 있습니다.
4. 파일을 읽은 후, 함수는 총 비용을 반환합니다. 현재 총 비용은 아직 실제 계산을 구현하지 않았기 때문에 0.0 으로 설정되어 있습니다.
5. 함수 외부에서 파일 이름 'portfolio.dat'를 사용하여 `portfolio_cost()` 함수를 호출합니다. 즉, `portfolio.dat` 파일의 데이터를 기반으로 총 비용을 계산하도록 함수에 요청하는 것입니다.
6. 마지막으로, f-string 을 사용하여 총 비용을 출력합니다.

이제 이 코드를 실행하여 어떤 작업을 수행하는지 확인해 보겠습니다. 다음 명령을 사용하여 터미널에서 Python 파일을 실행할 수 있습니다.

```bash
python3 ~/project/pcost.py
```

이 명령을 실행하면 `portfolio.dat` 파일의 각 줄이 터미널에 출력되고, 그 다음 현재 0.0 으로 설정된 총 비용이 출력됩니다. 이 출력은 파일이 올바르게 읽히고 있는지 확인하는 데 도움이 됩니다.
