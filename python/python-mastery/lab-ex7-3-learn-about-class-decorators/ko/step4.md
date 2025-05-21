# 행 변환 기능 추가

프로그래밍에서 특히 CSV 파일과 같은 소스의 데이터를 처리할 때 데이터 행에서 클래스의 인스턴스를 생성하는 것이 유용한 경우가 많습니다. 이 섹션에서는 `Structure` 클래스의 인스턴스를 데이터 행에서 생성하는 기능을 추가합니다. `Structure` 클래스에 `from_row` 클래스 메서드를 구현하여 이 작업을 수행합니다.

1. 먼저 `structure.py` 파일을 열어야 합니다. 여기에서 코드 변경을 수행합니다. 터미널에서 다음 명령을 사용합니다.

```bash
code ~/project/structure.py
```

2. 다음으로 `validate_attributes` 함수를 수정합니다. 이 함수는 `Validator` 인스턴스를 추출하고 `_fields` 및 `_types` 목록을 자동으로 빌드하는 클래스 데코레이터입니다. 또한 유형 정보를 수집하도록 업데이트합니다.

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

이 업데이트된 함수에서는 각 검증자에서 `expected_type` 속성을 수집하여 `_types` 클래스 변수에 저장합니다. 이는 나중에 행에서 올바른 유형으로 데이터를 변환할 때 유용합니다.

3. 이제 `from_row` 클래스 메서드를 `Structure` 클래스에 추가합니다. 이 메서드를 사용하면 목록 또는 튜플일 수 있는 데이터 행에서 클래스의 인스턴스를 생성할 수 있습니다.

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

이 메서드의 작동 방식은 다음과 같습니다.

- 목록 또는 튜플 형식일 수 있는 데이터 행을 가져옵니다.
- `_types` 목록에서 해당 함수를 사용하여 행의 각 값을 예상 유형으로 변환합니다.
- 그런 다음 변환된 값을 사용하여 클래스의 새 인스턴스를 생성하고 반환합니다.

4. 이러한 변경을 수행한 후 `structure.py` 파일을 저장합니다. 이렇게 하면 코드 변경 사항이 유지됩니다.

5. `from_row` 메서드가 예상대로 작동하는지 테스트해 보겠습니다. `Stock` 클래스를 사용하여 간단한 테스트를 만듭니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

다음과 유사한 출력이 표시됩니다.

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

문자열 값 '100'과 '490.1'이 자동으로 올바른 유형 (정수 및 부동 소수점) 으로 변환되었음을 확인하십시오. 이는 `from_row` 메서드가 올바르게 작동하고 있음을 보여줍니다.

6. 마지막으로 `reader.py` 모듈을 사용하여 CSV 파일에서 데이터를 읽어 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

CSV 파일의 주식을 보여주는 출력이 표시됩니다.

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

`from_row` 메서드를 사용하면 CSV 데이터를 `Stock` 클래스의 인스턴스로 쉽게 변환할 수 있습니다. `read_csv_as_instances` 함수와 결합하면 구조화된 데이터를 로드하고 작업하는 강력한 방법이 있습니다.
