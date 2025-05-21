# 구조에서 고급 초기화 구현

우리는 방금 함수 인수에 접근하기 위한 두 가지 강력한 기술을 배웠습니다. 이제 이러한 기술을 사용하여 `Structure` 클래스를 업데이트합니다. 먼저, 왜 이렇게 하는지 이해해 보겠습니다. 이러한 기술은 특히 다양한 유형의 인수를 처리할 때 클래스를 더 유연하고 사용하기 쉽게 만듭니다.

코드 편집기에서 `structure.py` 파일을 엽니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다. `cd` 명령은 디렉토리를 프로젝트 폴더로 변경하고, `code` 명령은 코드 편집기에서 `structure.py` 파일을 엽니다.

```bash
cd ~/project
code structure.py
```

파일의 내용을 다음 코드로 바꿉니다. 이 코드는 여러 메서드가 있는 `Structure` 클래스를 정의합니다. 각 부분을 살펴보고 무엇을 하는지 이해해 보겠습니다.

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

다음은 코드에서 수행한 작업입니다.

1. 이전 `__init__()` 메서드를 제거했습니다. 서브클래스가 자체 `__init__` 메서드를 정의하므로 더 이상 이전 메서드가 필요하지 않습니다.
2. 새로운 `_init()` 정적 메서드를 추가했습니다. 이 메서드는 프레임 검사를 사용하여 모든 매개변수를 자동으로 캡처하고 속성으로 설정합니다. 프레임 검사를 통해 호출 메서드의 지역 변수에 접근할 수 있습니다.
3. `__repr__()` 메서드를 유지했습니다. 이 메서드는 객체의 멋진 문자열 표현을 제공하며, 이는 디버깅 및 인쇄에 유용합니다.
4. `__setattr__()` 메서드를 추가했습니다. 이 메서드는 속성 유효성 검사를 적용하여 유효한 속성만 객체에 설정할 수 있도록 합니다.

이제 `Stock` 클래스를 업데이트해 보겠습니다. 다음 명령을 사용하여 `stock.py` 파일을 엽니다.

```bash
code stock.py
```

해당 내용을 다음 코드로 바꿉니다.

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

여기서 주요 변경 사항은 `__init__` 메서드가 각 속성을 수동으로 설정하는 대신 이제 `self._init()`를 호출한다는 것입니다. `_init()` 메서드는 프레임 검사를 사용하여 모든 매개변수를 자동으로 캡처하고 속성으로 설정합니다. 이렇게 하면 코드가 더 간결해지고 유지 관리가 쉬워집니다.

단위 테스트를 실행하여 구현을 테스트해 보겠습니다. 단위 테스트는 코드가 예상대로 작동하는지 확인하는 데 도움이 됩니다. 터미널에서 다음 명령을 실행합니다.

```bash
cd ~/project
python3 teststock.py
```

이전에는 실패했던 키워드 인수에 대한 테스트를 포함하여 모든 테스트가 통과하는 것을 볼 수 있습니다. 이는 구현이 올바르게 작동하고 있음을 의미합니다.

`Stock` 클래스에 대한 도움말 문서를 확인해 보겠습니다. 도움말 문서는 클래스 및 해당 메서드에 대한 정보를 제공합니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 -c "from stock import Stock; help(Stock)"
```

이제 모든 매개변수 이름을 표시하는 `__init__` 메서드에 대한 적절한 시그니처를 볼 수 있습니다. 이렇게 하면 다른 개발자가 클래스를 사용하는 방법을 더 쉽게 이해할 수 있습니다.

마지막으로, 키워드 인수가 예상대로 작동하는지 대화형으로 테스트해 보겠습니다. 터미널에서 다음 명령을 실행합니다.

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

지정된 속성으로 `Stock` 객체가 제대로 생성된 것을 볼 수 있습니다. 이는 클래스 초기화 시스템이 키워드 인수를 지원함을 확인합니다.

이 구현을 통해 다음과 같은 훨씬 더 유연하고 사용자 친화적인 클래스 초기화 시스템을 달성했습니다.

1. 문서에서 적절한 함수 시그니처를 유지하여 개발자가 클래스를 사용하는 방법을 더 쉽게 이해할 수 있도록 합니다.
2. 위치 인수와 키워드 인수를 모두 지원하여 객체를 생성할 때 더 많은 유연성을 제공합니다.
3. 서브클래스에서 최소한의 보일러플레이트 코드를 요구하여 작성해야 하는 코드의 양을 줄입니다.
