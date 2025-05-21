# 로깅 구현

이 단계에서는 코드를 개선할 것입니다. 간단한 print 메시지를 사용하는 대신, 적절한 로깅을 위해 Python 의 `logging` 모듈을 사용합니다. 로깅은 특히 오류를 처리하고 코드의 흐름을 이해하는 데 있어 프로그램이 수행하는 작업을 추적하는 훌륭한 방법입니다.

## 로깅 모듈 이해

Python 의 `logging` 모듈은 애플리케이션에서 로그 메시지를 보낼 수 있는 유연한 방법을 제공합니다. 간단한 print 문을 사용하는 것보다 훨씬 강력합니다. 다음과 같은 기능을 수행할 수 있습니다.

1. 다양한 로그 레벨 (DEBUG, INFO, WARNING, ERROR, CRITICAL): 이러한 레벨은 메시지의 중요도를 분류하는 데 도움이 됩니다. 예를 들어, DEBUG 는 개발 중에 유용한 자세한 정보를 위한 것이고, CRITICAL 은 프로그램을 중지시킬 수 있는 심각한 오류를 위한 것입니다.
2. 구성 가능한 출력 형식: 타임스탬프 또는 기타 유용한 정보를 추가하는 등 로그 메시지의 모양을 결정할 수 있습니다.
3. 메시지를 다른 출력 (콘솔, 파일 등) 으로 보낼 수 있습니다. 콘솔에 로그 메시지를 표시하거나, 파일에 저장하거나, 원격 서버로 보낼 수도 있습니다.
4. 심각도에 따른 로그 필터링: 로그 레벨에 따라 표시할 메시지를 제어할 수 있습니다.

## reader.py 에 로깅 추가

이제 로깅 모듈을 사용하도록 코드를 변경해 보겠습니다. `reader.py` 파일을 엽니다.

먼저 `logging` 모듈을 가져오고 이 모듈에 대한 로거를 설정해야 합니다. 파일 맨 위에 다음 코드를 추가합니다.

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

`import logging` 문은 `logging` 모듈을 가져와서 해당 함수를 사용할 수 있도록 합니다. `logging.getLogger(__name__)`은 이 특정 모듈에 대한 로거를 생성합니다. `__name__`을 사용하면 로거가 모듈과 관련된 고유한 이름을 갖게 됩니다.

다음으로, `convert_csv()` 함수를 수정하여 print 문 대신 로깅을 사용합니다. 업데이트된 코드는 다음과 같습니다.

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
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

여기서 주요 변경 사항은 다음과 같습니다.

- 오류 메시지에 대해 `print()`를 `logger.warning()`으로 바꿨습니다. 이렇게 하면 메시지가 적절한 경고 레벨로 기록되고 나중에 표시 여부를 제어할 수 있습니다.
- 예외에 대한 세부 정보를 포함하는 새로운 `logger.debug()` 메시지를 추가했습니다. 이렇게 하면 무엇이 잘못되었는지에 대한 자세한 정보를 얻을 수 있지만 로깅 레벨이 DEBUG 이하로 설정된 경우에만 표시됩니다.
- `str(e)`는 예외를 문자열로 변환하므로 로그 메시지에 오류 이유를 표시할 수 있습니다.

이러한 변경을 수행한 후 파일을 저장합니다.

## 로깅 테스트

로깅이 활성화된 상태에서 코드를 테스트해 보겠습니다. 터미널에서 다음 명령을 실행하여 Python 인터프리터를 엽니다.

```bash
python3
```

Python 인터프리터에 들어가면 다음 코드를 실행합니다.

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

여기서는 먼저 `logging` 모듈과 `reader` 모듈을 가져옵니다. 그런 다음 `logging.basicConfig(level=logging.DEBUG)`를 사용하여 로깅 레벨을 DEBUG 로 설정합니다. 즉, DEBUG, INFO, WARNING, ERROR 및 CRITICAL 을 포함한 모든 로그 메시지를 볼 수 있습니다. 그런 다음 `reader` 모듈에서 `read_csv_as_dicts` 함수를 호출하고 처리된 유효한 행의 수를 출력합니다.

다음과 같은 출력이 표시됩니다.

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

로깅 모듈이 각 메시지에 접두사를 추가하여 로그 레벨 (WARNING/DEBUG) 과 모듈 이름을 표시하는 것을 확인합니다.

이제 로그 레벨을 변경하여 경고만 표시하는 경우 어떻게 되는지 살펴보겠습니다. Python 인터프리터에서 다음 코드를 실행합니다.

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

이번에는 `logging.basicConfig(level=logging.WARNING)`를 사용하여 로깅 레벨을 WARNING 으로 설정했습니다. 이제 WARNING 메시지만 표시되고 DEBUG 메시지는 숨겨집니다.

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

이는 서로 다른 로깅 레벨을 사용하는 것의 장점을 보여줍니다. 코드를 변경하지 않고 로그에 표시되는 세부 정보를 제어할 수 있습니다.

Python 인터프리터를 종료하려면 다음 명령을 실행합니다.

```python
exit()
```

축하합니다! 이제 Python 프로그램에서 적절한 예외 처리 및 로깅을 구현했습니다. 이렇게 하면 코드가 더 안정적이고 오류가 발생할 때 더 나은 정보를 얻을 수 있습니다.
