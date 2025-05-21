# stock.py 프로그램 업데이트 및 테스트

이제 패키지를 만들고 내부 import 를 수정했으므로, 새로운 패키지 구조를 사용하도록 `stock.py` 파일을 업데이트할 차례입니다. Python 에서 패키지는 관련 모듈을 함께 구성하는 방법입니다. 코드베이스를 정리하고 코드를 더 쉽게 관리하고 재사용하는 데 도움이 됩니다.

편집기에서 `stock.py` 파일을 엽니다.

```bash
# 파일 탐색기에서 stock.py를 클릭하거나 실행:
code stock.py
```

`stock.py`의 현재 import 는 모든 파일이 동일한 디렉토리에 있던 이전 구조를 기반으로 합니다. Python 에서 모듈을 import 할 때 Python 은 특정 위치에서 모듈을 찾습니다. 이전 구조에서는 모든 파일이 동일한 디렉토리에 있었으므로 Python 이 모듈을 쉽게 찾을 수 있었습니다. 하지만 이제 새로운 패키지 구조를 사용하므로, `structly` 패키지 내에서 모듈을 찾을 위치를 Python 에 알려주도록 import 를 업데이트해야 합니다.

`stock.py` 파일을 다음과 정확히 일치하도록 업데이트합니다.

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

주요 변경 사항은 다음과 같습니다.

1. `from structure import Structure, String, PositiveInteger, PositiveFloat`를 `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`로 변경했습니다. 이 변경은 Python 에게 `structly` 패키지 내에서 `structure` 모듈을 찾도록 지시합니다.
2. `from reader import read_csv_as_instances`를 `from structly.reader import read_csv_as_instances`로 변경했습니다. 마찬가지로, 이 변경은 Python 이 `structly` 패키지 내에서 `reader` 모듈을 찾도록 지시합니다.
3. `from tableformat import create_formatter, print_table`을 `from structly.tableformat import create_formatter, print_table`로 변경했습니다. 이렇게 하면 Python 이 `structly` 패키지에서 `tableformat` 모듈을 찾을 수 있습니다.

이러한 변경을 수행한 후 파일을 저장합니다. 파일을 저장하는 것은 변경 사항이 저장되고 프로그램을 실행할 때 사용할 수 있도록 하기 때문에 중요합니다.

이제 모든 것이 올바르게 작동하는지 확인하기 위해 업데이트된 코드를 테스트해 보겠습니다.

```bash
python stock.py
```

다음 출력이 표시되어야 합니다.

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

이 출력이 표시되면 축하합니다! Python 패키지를 성공적으로 만들고 이를 사용하도록 코드를 업데이트했습니다. 즉, 코드가 이제 더 모듈 방식으로 구성되어 향후 유지 관리 및 확장이 더 쉬워졌습니다.
