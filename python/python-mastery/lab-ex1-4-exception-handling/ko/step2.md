# 오류 처리 추가하기

실제 데이터를 사용할 때는 불일치 또는 오류가 발생하는 경우가 매우 흔합니다. 예를 들어, 데이터에 누락된 값, 잘못된 형식 또는 기타 문제가 있을 수 있습니다. Python 은 이러한 상황을 적절하게 처리하기 위해 예외 처리 메커니즘을 제공합니다. 예외 처리를 사용하면 프로그램이 갑자기 중단되는 대신 오류가 발생하더라도 계속 실행될 수 있습니다.

## 문제 이해하기

`portfolio3.dat` 파일을 살펴보겠습니다. 이 파일에는 주식 기호, 주식 수, 주당 가격과 같은 포트폴리오에 대한 일부 데이터가 포함되어 있습니다. 이 파일의 내용을 보려면 다음 명령을 사용할 수 있습니다.

```bash
cat /home/labex/project/portfolio3.dat
```

이 명령을 실행하면 파일의 일부 줄에 주식 수 대신 대시 (`-`) 가 있는 것을 알 수 있습니다. 다음은 표시될 수 있는 예입니다.

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

이 파일에서 현재 코드를 실행하려고 하면 충돌이 발생합니다. 그 이유는 코드에서 주식 수를 정수로 변환하려고 하지만 대시 (`-`) 를 정수로 변환할 수 없기 때문입니다. 코드를 실행하고 어떤 일이 발생하는지 살펴보겠습니다.

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

다음과 같은 오류 메시지가 표시됩니다.

```
ValueError: invalid literal for int() with base 10: '-'
```

이 오류는 Python 이 `int(fields[1])`을 실행하려고 할 때 `-` 문자를 정수로 변환할 수 없기 때문에 발생합니다.

## 예외 처리 소개

Python 의 예외 처리는 `try` 및 `except` 블록을 사용합니다. `try` 블록에는 예외를 발생시킬 수 있는 코드가 포함되어 있습니다. 예외는 프로그램 실행 중에 발생하는 오류입니다. `except` 블록에는 `try` 블록에서 예외가 발생할 경우 실행될 코드가 포함되어 있습니다.

`try` 및 `except` 블록이 작동하는 방식의 예는 다음과 같습니다.

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
```

Python 이 `try` 블록의 코드를 실행할 때 예외가 발생하면 실행이 즉시 일치하는 `except` 블록으로 이동합니다. `except` 블록의 `ExceptionType`은 처리하려는 예외 유형을 지정합니다. 변수 `e`에는 오류 메시지와 같은 예외에 대한 정보가 포함되어 있습니다.

## 예외 처리를 사용하여 함수 수정하기

데이터의 오류를 처리하도록 `pcost.py` 파일을 업데이트해 보겠습니다. `try` 및 `except` 블록을 사용하여 잘못된 데이터가 있는 줄을 건너뛰고 경고 메시지를 표시합니다.

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    Handles lines with bad data by skipping them and showing a warning.

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
            try:
                # Extract the data (symbol, shares, price)
                shares = int(fields[1])
                price = float(fields[2])
                # Add the cost to our running total
                total_cost += shares * price
            except ValueError as e:
                # Print a warning for lines that can't be parsed
                print(f"Couldn't parse: '{line}'")
                print(f"Reason: {e}")

    return total_cost

# Call the function with the portfolio3.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

이 업데이트된 코드에서는 먼저 파일을 열고 줄 단위로 읽습니다. 각 줄에 대해 필드로 분할합니다. 그런 다음 주식 수를 정수로, 가격을 부동 소수점으로 변환하려고 시도합니다. 이 변환이 실패하면 (즉, `ValueError`가 발생하면) 경고 메시지를 출력하고 해당 줄을 건너뜁니다. 그렇지 않으면 주식 비용을 계산하여 총 비용에 추가합니다.

## 업데이트된 함수 테스트하기

이제 문제가 있는 파일로 업데이트된 프로그램을 실행해 보겠습니다. 먼저 프로젝트 디렉토리로 이동한 다음 Python 스크립트를 실행할 수 있습니다.

```bash
cd /home/labex/project
python3 pcost.py
```

다음과 같은 출력이 표시됩니다.

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

이제 프로그램은 다음을 수행합니다.

1.  파일의 각 줄을 처리하려고 시도합니다.
2.  줄에 잘못된 데이터가 포함된 경우 `ValueError`를 catch 합니다.
3.  문제에 대한 유용한 메시지를 출력합니다.
4.  파일의 나머지 부분을 계속 처리합니다.
5.  유효한 줄을 기반으로 총 비용을 반환합니다.

이 접근 방식을 사용하면 불완전한 데이터를 처리할 때 프로그램이 훨씬 더 강력해집니다. 오류를 적절하게 처리하고 여전히 유용한 결과를 제공할 수 있습니다.
