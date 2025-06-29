# 코루틴 파이프라인 구성 요소 생성

이 단계에서는 주식 데이터를 처리하기 위해 더 특화된 코루틴을 생성할 것입니다. 코루틴은 실행을 일시 중지하고 재개할 수 있는 특수한 유형의 함수로, 데이터 처리 파이프라인을 구축하는 데 매우 유용합니다. 우리가 생성하는 각 코루틴은 전체 처리 파이프라인에서 특정 작업을 수행합니다.

1. 먼저, 새 파일을 생성해야 합니다. `/home/labex/project` 디렉토리로 이동하여 `coticker.py`라는 파일을 만듭니다. 이 파일은 코루틴 기반 데이터 처리를 위한 모든 코드를 담을 것입니다.

2. 이제 `coticker.py` 파일에 코드를 작성하기 시작해 보겠습니다. 먼저 필요한 모듈을 가져오고 기본 구조를 정의합니다. 모듈은 유용한 함수와 클래스를 제공하는 미리 작성된 코드 라이브러리입니다. 다음 코드가 바로 그 역할을 합니다.

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. 위 코드를 보면 `String()`, `Float()`, `Integer()`와 관련된 오류가 있음을 알 수 있습니다. 이것들은 우리가 가져와야 하는 클래스입니다. 따라서 파일 상단에 필요한 import 문을 추가합니다. 이렇게 하면 파이썬이 이러한 클래스를 어디에서 찾아야 하는지 알 수 있습니다. 업데이트된 코드는 다음과 같습니다.

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. 다음으로, 데이터 처리 파이프라인을 형성할 코루틴 구성 요소를 추가합니다. 각 코루틴은 파이프라인에서 특정 작업을 수행합니다. 다음은 이러한 코루틴을 추가하는 코드입니다.

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. 각 코루틴이 무엇을 하는지 이해해 보겠습니다.
   - `to_csv`: 이 코루틴의 역할은 원시 텍스트 줄을 구문 분석된 CSV 행으로 변환하는 것입니다. 데이터가 처음에 텍스트 형식으로 되어 있고 이를 구조화된 CSV 데이터로 분해해야 하므로 중요합니다.
   - `create_ticker`: 이 코루틴은 CSV 행을 가져와서 `Ticker` 객체를 생성합니다. `Ticker` 객체는 주식 데이터를 더 체계적인 방식으로 나타냅니다.
   - `negchange`: `Ticker` 객체를 필터링합니다. 음수 가격 변동이 있는 주식만 전달합니다. 이를 통해 가치가 하락하는 주식에 집중할 수 있습니다.
   - `ticker`: 이 코루틴은 티커 데이터를 형식화하고 표시합니다. 포매터를 사용하여 데이터를 보기 좋고 읽기 쉬운 표로 표시합니다.

6. 마지막으로, 이러한 모든 구성 요소를 함께 연결하는 메인 프로그램 코드를 추가해야 합니다. 이 코드는 파이프라인을 통해 데이터 흐름을 설정합니다. 다음은 코드입니다.

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change']

    # Create the processing pipeline
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # Connect the pipeline to the data source
    follow('stocklog.csv', csv_parser)
```

7. 모든 코드를 작성한 후 `coticker.py` 파일을 저장합니다. 그런 다음 터미널을 열고 다음 명령을 실행합니다. `cd` 명령은 파일이 있는 디렉토리로 디렉토리를 변경하고, `python3` 명령은 파이썬 스크립트를 실행합니다.

```bash
cd /home/labex/project
python3 coticker.py
```

8. 모든 것이 잘 진행되면 터미널에 형식화된 표가 표시됩니다. 이 표는 음수 가격 변동이 있는 주식을 보여줍니다. 출력은 다음과 유사합니다.

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

표의 실제 값은 생성된 주식 데이터에 따라 달라질 수 있습니다.

## 파이프라인 흐름 이해

이 프로그램에서 가장 중요한 부분은 데이터가 코루틴을 통해 어떻게 흐르는지입니다. 단계별로 살펴보겠습니다.

1. `follow` 함수는 `stocklog.csv` 파일에서 줄을 읽는 것으로 시작합니다. 이것이 우리의 데이터 소스입니다.
2. 읽은 각 줄은 `csv_parser` 코루틴으로 전송됩니다. `csv_parser`는 원시 텍스트 줄을 가져와 CSV 필드로 구문 분석합니다.
3. 구문 분석된 CSV 데이터는 `tick_creator` 코루틴으로 전송됩니다. 이 코루틴은 CSV 행에서 `Ticker` 객체를 생성합니다.
4. `Ticker` 객체는 `neg_filter` 코루틴으로 전송됩니다. 이 코루틴은 각 `Ticker` 객체를 확인합니다. 주식의 가격 변동이 음수이면 객체를 전달하고, 그렇지 않으면 폐기합니다.
5. 마지막으로, 필터링된 `Ticker` 객체는 `ticker` 코루틴으로 전송됩니다. `ticker` 코루틴은 데이터를 형식화하고 표로 표시합니다.

이 파이프라인 아키텍처는 각 구성 요소가 단일 작업에 집중할 수 있기 때문에 매우 유용합니다. 이렇게 하면 코드가 더 모듈화되어 이해, 수정 및 유지 관리가 더 쉬워집니다.
