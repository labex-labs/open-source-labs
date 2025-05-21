# 추상 기본 클래스 (Abstract Base Class) 구현하기

이 단계에서는 Python 의 `abc` 모듈을 사용하여 `TableFormatter` 클래스를 적절한 추상 기본 클래스 (ABC) 로 변환할 것입니다. 하지만 먼저 추상 기본 클래스가 무엇이며 왜 필요한지 이해해 보겠습니다.

## 추상 기본 클래스 이해하기

추상 기본 클래스는 Python 의 특수한 유형의 클래스입니다. 직접 객체를 생성할 수 없는 클래스이므로 인스턴스화할 수 없습니다. 추상 기본 클래스의 주요 목적은 서브클래스에 대한 공통 인터페이스를 정의하는 것입니다. 모든 서브클래스가 따라야 하는 규칙 집합을 설정합니다. 특히, 서브클래스가 특정 메서드를 구현하도록 요구합니다.

추상 기본 클래스에 대한 몇 가지 주요 개념은 다음과 같습니다.

- Python 에서 추상 기본 클래스를 생성하기 위해 `abc` 모듈을 사용합니다.
- `@abstractmethod` 데코레이터로 표시된 메서드는 규칙과 같습니다. 추상 기본 클래스에서 상속받는 모든 서브클래스는 이러한 메서드를 구현해야 합니다.
- 추상 기본 클래스에서 상속받았지만 필요한 모든 메서드를 구현하지 않은 클래스의 객체를 생성하려고 하면 Python 에서 오류가 발생합니다.

이제 추상 기본 클래스의 기본 사항을 이해했으므로 `TableFormatter` 클래스를 수정하여 추상 기본 클래스가 되는 방법을 살펴보겠습니다.

## TableFormatter 클래스 수정하기

`tableformat.py` 파일을 엽니다. `TableFormatter` 클래스를 변경하여 `abc` 모듈을 사용하고 추상 기본 클래스가 되도록 할 것입니다.

1. 먼저, `abc` 모듈에서 필요한 것을 가져와야 합니다. 파일 상단에 다음 import 문을 추가합니다.

```python
# tableformat.py
from abc import ABC, abstractmethod
```

이 import 문은 두 가지 중요한 사항을 가져옵니다. `ABC`는 Python 의 모든 추상 기본 클래스의 기본 클래스이고, `abstractmethod`는 메서드를 추상으로 표시하는 데 사용할 데코레이터입니다.

2. 다음으로, `TableFormatter` 클래스를 수정합니다. 추상 기본 클래스가 되려면 `ABC`에서 상속받아야 하며, `@abstractmethod` 데코레이터를 사용하여 메서드를 추상으로 표시합니다. 수정된 클래스는 다음과 같아야 합니다.

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

이 수정된 클래스에 대해 몇 가지 사항에 유의하십시오.

- 클래스는 이제 `ABC`에서 상속받으므로 공식적으로 추상 기본 클래스입니다.
- `headings` 및 `row` 메서드는 모두 `@abstractmethod`로 데코레이트됩니다. 이는 `TableFormatter`의 모든 서브클래스가 이러한 메서드를 구현해야 함을 Python 에 알려줍니다.
- `NotImplementedError`를 `pass`로 대체했습니다. `@abstractmethod` 데코레이터는 서브클래스가 이러한 메서드를 구현하도록 하는 역할을 하므로 더 이상 `NotImplementedError`가 필요하지 않습니다.

## 추상 기본 클래스 테스트하기

이제 `TableFormatter` 클래스를 추상 기본 클래스로 만들었으므로 제대로 작동하는지 테스트해 보겠습니다. 다음 코드를 사용하여 `test_abc.py`라는 파일을 만들 것입니다.

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

이 코드에는 두 가지 테스트 케이스가 있습니다. 첫 번째 테스트 케이스는 `TableFormatter`에서 상속받으려고 하지만 메서드 이름이 잘못된 `NewFormatter` 클래스를 정의합니다. 두 번째 테스트 케이스는 필요한 모든 메서드를 올바르게 구현하는 `ProperFormatter` 클래스를 정의합니다.

테스트를 실행하려면 터미널을 열고 다음 명령을 실행합니다.

```bash
python test_abc.py
```

다음과 유사한 출력이 표시됩니다.

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

이 출력은 추상 기본 클래스가 예상대로 작동함을 확인합니다. 첫 번째 테스트 케이스는 `NewFormatter` 클래스가 `headings` 메서드를 올바르게 구현하지 않았기 때문에 실패합니다. 두 번째 테스트 케이스는 `ProperFormatter` 클래스가 필요한 모든 메서드를 구현했기 때문에 통과합니다.
