# 예외 처리 구현

이 단계에서는 코드를 더욱 강력하게 만드는 데 집중하겠습니다. 프로그램이 잘못된 데이터를 만나면 종종 충돌합니다. 그러나 예외 처리 (exception handling) 라는 기술을 사용하여 이러한 문제를 적절하게 처리할 수 있습니다. 이를 구현하기 위해 `reader.py` 파일을 수정합니다. 예외 처리를 통해 프로그램은 예기치 않은 데이터에 직면하더라도 갑자기 중단되는 대신 계속 실행될 수 있습니다.

## Try-Except 블록 이해

Python 은 try-except 블록을 사용하여 예외를 처리하는 강력한 방법을 제공합니다. 작동 방식을 자세히 살펴보겠습니다.

```python
try:
    # 예외를 발생시킬 수 있는 코드
    result = risky_operation()
except SomeExceptionType as e:
    # 예외가 발생할 경우 실행되는 코드
    handle_exception(e)
```

`try` 블록에는 예외를 발생시킬 수 있는 코드를 넣습니다. 예외는 프로그램 실행 중에 발생하는 오류입니다. 예를 들어, 숫자를 0 으로 나누려고 하면 Python 은 `ZeroDivisionError` 예외를 발생시킵니다. `try` 블록에서 예외가 발생하면 Python 은 `try` 블록의 코드 실행을 중단하고 일치하는 `except` 블록으로 이동합니다. `except` 블록에는 예외를 처리하는 코드가 포함되어 있습니다. `SomeExceptionType`은 잡으려는 예외의 유형입니다. 특정 유형의 예외를 잡거나 일반 `Exception`을 사용하여 모든 유형의 예외를 잡을 수 있습니다. `as e` 부분은 오류에 대한 정보가 포함된 예외 객체에 액세스할 수 있도록 합니다.

## 코드 수정

이제 try-except 블록에 대해 배운 내용을 `convert_csv()` 함수에 적용해 보겠습니다. 편집기에서 `reader.py` 파일을 엽니다.

1. 현재 `convert_csv()` 함수를 다음 코드로 바꿉니다.

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

이 새로운 구현에서:

- 각 행을 처리하기 위해 `map()` 대신 `for` 루프를 사용합니다. 이렇게 하면 각 행의 처리를 더 잘 제어할 수 있습니다.
- 변환 코드를 try-except 블록으로 묶습니다. 즉, 행 변환 중에 예외가 발생하더라도 프로그램이 충돌하지 않습니다. 대신 `except` 블록으로 이동합니다.
- `except` 블록에서 잘못된 행에 대한 오류 메시지를 출력합니다. 이렇게 하면 문제가 있는 행을 식별하는 데 도움이 됩니다.
- 오류 메시지를 출력한 후 `continue` 문을 사용하여 현재 행을 건너뛰고 나머지 행 처리를 계속합니다.

이러한 변경을 수행한 후 파일을 저장합니다.

## 변경 사항 테스트

`missing.csv` 파일로 수정된 코드를 테스트해 보겠습니다. 먼저 터미널에서 다음 명령을 실행하여 Python 인터프리터를 엽니다.

```bash
python3
```

Python 인터프리터에 들어가면 다음 코드를 실행합니다.

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

이 코드를 실행하면 문제가 있는 각 행에 대한 오류 메시지가 표시됩니다. 그러나 프로그램은 계속 처리하고 유효한 행을 반환합니다. 다음은 표시될 수 있는 예입니다.

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

또한 프로그램이 유효한 데이터로 올바르게 작동하는지 확인해 보겠습니다. Python 인터프리터에서 다음 코드를 실행합니다.

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

모든 행이 오류 없이 처리되는 것을 볼 수 있습니다. 다음은 출력의 예입니다.

```
Number of valid rows processed: 17
```

Python 인터프리터를 종료하려면 다음 명령을 실행합니다.

```python
exit()
```

이제 코드가 더 강력해졌습니다. 충돌하는 대신 잘못된 행을 건너뛰어 잘못된 데이터를 적절하게 처리할 수 있습니다. 이렇게 하면 프로그램의 신뢰성과 사용자 편의성이 향상됩니다.
