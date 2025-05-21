# 코루틴 파이프라인 향상

이제 기본 파이프라인이 실행되고 있으므로, 이를 더욱 유연하게 만들 차례입니다. 프로그래밍에서 유연성은 다양한 요구 사항에 맞게 코드를 조정할 수 있도록 하므로 매우 중요합니다. `coticker.py` 프로그램을 수정하여 다양한 필터링 및 형식 지정 옵션을 지원함으로써 이를 달성할 것입니다.

1. 먼저, 코드 편집기에서 `coticker.py` 파일을 엽니다. 코드 편집기는 프로그램에 필요한 모든 변경을 수행하는 곳입니다. 코드를 보고, 편집하고, 저장할 수 있는 편리한 환경을 제공합니다.

2. 다음으로, 주식 이름으로 데이터를 필터링하는 새 코루틴을 추가합니다. 코루틴은 실행을 일시 중지하고 재개할 수 있는 특수한 유형의 함수입니다. 이를 통해 서로 다른 처리 단계를 거쳐 데이터가 흐를 수 있는 파이프라인을 만들 수 있습니다. 다음은 새 코루틴에 대한 코드입니다.

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

이 코드에서 `filter_by_name` 코루틴은 주식 이름과 대상 코루틴을 매개변수로 사용합니다. `yield` 키워드를 사용하여 레코드를 지속적으로 기다립니다. 레코드가 도착하면 레코드의 이름이 지정된 이름과 일치하는지 확인합니다. 일치하는 경우 레코드를 대상 코루틴으로 보냅니다.

3. 이제 가격 임계값을 기반으로 필터링하는 또 다른 코루틴을 추가해 보겠습니다. 이 코루틴은 특정 가격 범위 내의 주식을 선택하는 데 도움이 됩니다. 다음은 코드입니다.

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

이전 코루틴과 유사하게, `price_threshold` 코루틴은 레코드를 기다립니다. 그런 다음 레코드의 가격이 지정된 최소 및 최대 가격 범위 내에 있는지 확인합니다. 그렇다면 레코드를 대상 코루틴으로 보냅니다.

4. 새 코루틴을 추가한 후, 이러한 추가 필터를 시연하기 위해 메인 프로그램을 업데이트해야 합니다. 메인 프로그램은 애플리케이션의 진입점이며, 여기서 처리 파이프라인을 설정하고 데이터 흐름을 시작합니다. 다음은 업데이트된 코드입니다.

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change', 'high', 'low']

    # Create the processing pipeline with multiple outputs

    # Pipeline 1: Show all negative changes (same as before)
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # Start following the file with the first pipeline
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # Wait a moment to see some results
    import time
    time.sleep(5)

    # Pipeline 2: Filter by name (AAPL)
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # Follow the file with the second pipeline
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # Wait a moment to see some results
    time.sleep(5)

    # Pipeline 3: Filter by price range
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # Follow with the third pipeline
    follow('stocklog.csv', csv_parser3)
```

이 업데이트된 코드에서는 세 가지 다른 처리 파이프라인을 생성합니다. 첫 번째 파이프라인은 음수 변동이 있는 주식을 표시하고, 두 번째 파이프라인은 'AAPL' 이름으로 주식을 필터링하며, 세 번째 파이프라인은 50 에서 75 사이의 가격 범위를 기반으로 주식을 필터링합니다. 스레드를 사용하여 처음 두 파이프라인을 동시에 실행하여 데이터를 보다 효율적으로 처리할 수 있습니다.

5. 모든 변경을 완료했으면 파일을 저장합니다. 파일을 저장하면 모든 수정 사항이 보존됩니다. 그런 다음 터미널에서 다음 명령을 사용하여 업데이트된 프로그램을 실행합니다.

```bash
cd /home/labex/project
python3 coticker.py
```

`cd` 명령은 현재 디렉토리를 프로젝트 디렉토리로 변경하고, `python3 coticker.py` 명령은 파이썬 프로그램을 실행합니다.

6. 프로그램을 실행한 후 세 가지 다른 출력을 볼 수 있습니다.
   - 먼저, 음수 변동이 있는 주식을 볼 수 있습니다.
   - 그런 다음, 모든 AAPL 주식 업데이트를 볼 수 있습니다.
   - 마지막으로, 50 에서 75 사이의 가격으로 책정된 모든 주식을 볼 수 있습니다.

## 향상된 파이프라인 이해

향상된 프로그램은 몇 가지 중요한 개념을 보여줍니다.

1. **다중 파이프라인 (Multiple Pipelines)**: 동일한 데이터 소스에서 여러 처리 파이프라인을 생성할 수 있습니다. 이를 통해 동일한 데이터에 대해 서로 다른 유형의 분석을 동시에 수행할 수 있습니다.
2. **특수 필터 (Specialized Filters)**: 특정 필터링 작업을 위해 서로 다른 코루틴을 생성할 수 있습니다. 이러한 필터는 특정 기준을 충족하는 데이터만 선택하는 데 도움이 됩니다.
3. **동시 처리 (Concurrent Processing)**: 스레드를 사용하여 여러 파이프라인을 동시에 실행할 수 있습니다. 이렇게 하면 데이터를 병렬로 처리하여 프로그램의 효율성을 향상시킬 수 있습니다.
4. **파이프라인 구성 (Pipeline Composition)**: 코루틴은 서로 다른 데이터 처리 목표를 달성하기 위해 다양한 방식으로 결합될 수 있습니다. 이를 통해 필요에 따라 데이터 처리 파이프라인을 사용자 정의할 수 있는 유연성을 얻을 수 있습니다.

이 접근 방식은 스트리밍 데이터를 처리하는 유연하고 모듈식인 방법을 제공합니다. 프로그램의 전체 아키텍처를 변경하지 않고도 처리 단계를 추가하거나 수정할 수 있습니다.
