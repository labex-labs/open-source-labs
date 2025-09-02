# 행 변환 기능 추가

프로그래밍에서는 특히 CSV 파일과 같은 소스의 데이터를 다룰 때 데이터 행에서 클래스 인스턴스를 만드는 것이 유용한 경우가 많습니다. 이 섹션에서는 `Structure` 클래스의 인스턴스를 데이터 행에서 만들 수 있는 기능을 추가합니다. `Structure` 클래스에 `from_row` 클래스 메서드를 구현하여 이를 수행할 것입니다.

1. 먼저 편집기에서 `structure.py` 파일을 엽니다. 이곳에서 코드 변경을 수행할 것입니다.

2. 다음으로 `validate_attributes` 함수를 수정합니다. 이 함수는 `Validator` 인스턴스를 추출하고 `_fields` 및 `_types` 목록을 자동으로 빌드하는 클래스 데코레이터입니다. 유형 정보도 수집하도록 업데이트할 것입니다.

```python
def validate_attributes(cls):
    """
    Validator 인스턴스를 추출하고 _fields 및 _types 목록을 자동으로 빌드하는
    클래스 데코레이터
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # 검증자 이름을 기반으로 _fields 설정
    cls._fields = [val.name for val in validators]

    # 검증자 expected_types 를 기반으로 _types 설정
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # 초기화 메서드 생성
    cls.create_init()

    return cls
```

이 업데이트된 함수에서는 각 검증자로부터 `expected_type` 속성을 수집하여 `_types` 클래스 변수에 저장합니다. 이는 나중에 행에서 올바른 유형으로 데이터를 변환할 때 유용할 것입니다.

3. 이제 `Structure` 클래스에 `from_row` 클래스 메서드를 추가합니다. 이 메서드를 사용하면 목록 또는 튜플일 수 있는 데이터 행에서 클래스의 인스턴스를 만들 수 있습니다.

```python
@classmethod
def from_row(cls, row):
    """
    데이터 행 (목록 또는 튜플) 에서 인스턴스 생성
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

이 메서드는 다음과 같이 작동합니다.

- 목록 또는 튜플 형식일 수 있는 데이터 행을 가져옵니다.
- `_types` 목록의 해당 함수를 사용하여 행의 각 값을 예상 유형으로 변환합니다.
- 그런 다음 변환된 값을 사용하여 클래스의 새 인스턴스를 만들고 반환합니다.

4. 이러한 변경을 한 후 `structure.py` 파일을 저장합니다. 이렇게 하면 코드 변경 사항이 보존됩니다.

5. `from_row` 메서드가 예상대로 작동하는지 확인하기 위해 테스트해 보겠습니다. `Stock` 클래스를 사용하여 간단한 테스트를 만들 것입니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

다음과 유사한 출력이 표시되어야 합니다.

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

문자열 값 '100'과 '490.1'이 올바른 유형 (정수 및 부동 소수점) 으로 자동 변환되었음을 알 수 있습니다. 이는 `from_row` 메서드가 올바르게 작동하고 있음을 보여줍니다.

6. 마지막으로 `reader.py` 모듈을 사용하여 CSV 파일에서 데이터를 읽어 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

CSV 파일의 주식을 보여주는 출력이 표시되어야 합니다.

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 82391.5
```

`from_row` 메서드를 사용하면 CSV 데이터를 `Stock` 클래스의 인스턴스로 쉽게 변환할 수 있습니다. `read_csv_as_instances` 함수와 결합하면 구조화된 데이터를 로드하고 작업하는 강력한 방법을 갖게 됩니다.
