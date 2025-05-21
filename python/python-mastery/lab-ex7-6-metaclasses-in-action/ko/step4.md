# 구현 테스트

이제 메타클래스를 구현하고 `Structure` 클래스를 수정했으므로 구현을 테스트할 차례입니다. 테스트는 모든 것이 제대로 작동하는지 확인하는 데 도움이 되므로 매우 중요합니다. 테스트를 실행함으로써 잠재적인 문제를 조기에 파악하고 코드가 예상대로 작동하는지 확인할 수 있습니다.

먼저, 유닛 테스트를 실행하여 `Stock` 클래스가 예상대로 작동하는지 확인해 보겠습니다. 유닛 테스트는 코드의 개별 부분을 확인하는 작고 격리된 테스트입니다. 이 경우 `Stock` 클래스가 올바르게 작동하는지 확인하려고 합니다. 유닛 테스트를 실행하려면 터미널에서 다음 명령을 사용합니다.

```bash
python3 teststock.py
```

모든 것이 제대로 작동하면 모든 테스트가 오류 없이 통과해야 합니다. 테스트가 성공적으로 실행되면 출력은 다음과 유사해야 합니다.

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

점은 통과된 각 테스트를 나타내고, 마지막 `OK`는 모든 테스트가 성공했음을 나타냅니다.

이제 실제 데이터와 테이블 형식 기능을 사용하여 `Stock` 클래스를 테스트해 보겠습니다. 이렇게 하면 `Stock` 클래스가 데이터와 상호 작용하는 방식과 테이블 형식이 작동하는 방식을 확인할 수 있는 보다 실제적인 시나리오를 얻을 수 있습니다. 터미널에서 다음 명령을 사용합니다.

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Read portfolio data into Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Format and print the portfolio data
print('\nFormatted table:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

이 코드에서는 먼저 필요한 클래스와 함수를 가져옵니다. 그런 다음 CSV 파일에서 데이터를 `Stock` 인스턴스로 읽습니다. 그 후 포트폴리오 데이터를 출력한 다음 테이블 형식으로 지정하고 형식화된 테이블을 출력합니다.

다음과 유사한 출력이 표시되어야 합니다.

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

잠시 시간을 내어 우리가 달성한 것을 생각해 보십시오.

1. 모든 검증자 유형을 자동으로 수집하는 메커니즘을 만들었습니다. 즉, 모든 검증자를 수동으로 추적할 필요가 없으므로 시간과 오류 발생 가능성을 줄일 수 있습니다.
2. 이러한 유형을 `Structure` 하위 클래스의 네임스페이스에 주입하는 메타클래스를 구현했습니다. 이를 통해 하위 클래스는 이러한 검증자를 명시적으로 가져올 필요 없이 사용할 수 있습니다.
3. 검증자 유형을 명시적으로 가져올 필요가 없어졌습니다. 이렇게 하면 코드가 더 깔끔하고 읽기 쉬워집니다.
4. 이 모든 작업이 백그라운드에서 수행되므로 새로운 구조를 정의하는 코드가 깔끔하고 간단해집니다.

최종 `stock.py` 파일은 메타클래스가 없었을 때보다 훨씬 깔끔합니다.

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

검증자 유형을 직접 가져올 필요가 없으므로 코드가 더 간결하고 유지 관리하기 쉽습니다. 이것은 메타클래스가 코드의 품질을 향상시킬 수 있는 좋은 예입니다.
