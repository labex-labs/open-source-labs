# 프로그램 마무리

이제 코드를 정리하고 `pcost.py` 프로그램의 최종 버전을 만들 것입니다. 코드를 정리한다는 것은 불필요한 부분을 제거하고 출력이 보기 좋게 보이도록 하는 것을 의미합니다. 이는 코드를 더 전문적이고 이해하기 쉽게 만들므로 프로그래밍에서 중요한 단계입니다.

먼저 디버그 print 문을 제거합니다. 이러한 문은 변수 값과 프로그램의 흐름을 확인하기 위해 개발 중에 사용되지만 최종 버전에서는 필요하지 않습니다. 그런 다음 최종 출력이 깔끔하게 형식화되었는지 확인합니다.

다음은 `pcost.py` 코드의 최종 버전입니다.

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    try:
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

                # Calculate the cost of this stock purchase and add to the total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Return the total cost
    return total_cost

# Main block to run when the script is executed directly
if __name__ == '__main__':
    # Call the function with the portfolio file
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

이 코드의 최종 버전에는 몇 가지 개선 사항이 있습니다.

1.  오류 처리: 두 가지 유형의 오류를 포착하는 코드를 추가했습니다. `FileNotFoundError`는 지정된 파일이 존재하지 않을 때 발생합니다. 이 경우 프로그램은 오류 메시지를 출력하고 0.0 을 반환합니다. `Exception` 블록은 파일을 처리하는 동안 발생할 수 있는 다른 모든 오류를 포착합니다. 이렇게 하면 프로그램이 더 강력해지고 예기치 않게 충돌할 가능성이 줄어듭니다.
2.  적절한 형식 지정: 총 비용은 f-string 에서 `:.2f` 형식 지정자를 사용하여 소수점 두 자리로 형식화됩니다. 이렇게 하면 출력이 더 전문적으로 보이고 읽기 쉬워집니다.
3.  `__name__ == '__main__'` 확인: 이는 일반적인 Python 관용구입니다. 이 블록 내부의 코드가 스크립트가 직접 실행될 때만 실행되도록 합니다. 스크립트가 다른 스크립트로 모듈로 가져온 경우 이 코드는 실행되지 않습니다. 이를 통해 스크립트의 동작을 더 잘 제어할 수 있습니다.

이제 최종 코드를 실행해 보겠습니다. 터미널을 열고 다음 명령을 입력합니다.

```bash
python3 ~/project/pcost.py
```

이 명령을 실행하면 프로그램은 `portfolio.dat` 파일을 읽고, 포트폴리오의 총 비용을 계산하고, 결과를 출력합니다. 포트폴리오의 총 비용이 표시되어야 하며, 이는 $44671.15 여야 합니다.

축하합니다! 파일에서 데이터를 읽고, 처리하고, 결과를 계산하는 Python 프로그램을 성공적으로 만들었습니다. 이는 훌륭한 성과이며, 숙련된 Python 프로그래머가 되기 위한 여정에 있다는 것을 보여줍니다.
