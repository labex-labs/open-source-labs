# 문제 이해

메타클래스를 탐구하기 전에, 해결하려는 문제를 이해하는 것이 중요합니다. 프로그래밍에서 우리는 종종 속성에 특정 유형을 가진 구조를 생성해야 합니다. 이전 작업에서 우리는 유형 검사 (type-checked) 구조를 위한 시스템을 개발했습니다. 이 시스템을 사용하면 각 속성이 특정 유형을 가지며, 이러한 속성에 할당된 값이 해당 유형에 따라 검증되는 클래스를 정의할 수 있습니다.

다음은 이 시스템을 사용하여 `Stock` 클래스를 생성하는 예입니다.

```python
from validate import String, PositiveInteger, PositiveFloat
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

이 코드에서 먼저 `validate` 모듈에서 검증자 유형 (`String`, `PositiveInteger`, `PositiveFloat`) 을 가져오고, `structure` 모듈에서 `Structure` 클래스를 가져옵니다. 그런 다음 `Structure`에서 상속받는 `Stock` 클래스를 정의합니다. `Stock` 클래스 내에서 특정 검증자 유형을 가진 속성을 정의합니다. 예를 들어, `name` 속성은 문자열이어야 하고, `shares`는 양의 정수여야 하며, `price`는 양의 부동 소수점 숫자여야 합니다.

그러나 이 접근 방식에는 문제가 있습니다. 파일 상단에서 모든 검증자 유형을 가져와야 합니다. 실제 시나리오에서 검증자 유형을 더 많이 추가할수록 이러한 가져오기가 매우 길어지고 관리하기 어려워질 수 있습니다. 이는 `from validate import *`를 사용하게 될 수 있는데, 이는 이름 충돌을 일으키고 코드를 덜 읽기 쉽게 만들 수 있으므로 일반적으로 권장되지 않는 방식입니다.

시작점을 이해하기 위해 `Structure` 클래스를 살펴보겠습니다. 편집기에서 `structure.py` 파일을 열고 내용을 검토해야 합니다. 이렇게 하면 메타클래스 기능을 추가하기 전에 기본 구조 처리가 어떻게 구현되는지 확인할 수 있습니다.

```bash
code structure.py
```

파일을 열면 `Structure` 클래스의 기본 구현을 볼 수 있습니다. 이 클래스는 속성 초기화를 처리하지만 아직 메타클래스 기능이 없습니다.

다음으로, 검증자 클래스를 살펴보겠습니다. 이러한 클래스는 `validate.py` 파일에 정의되어 있습니다. 이미 디스크립터 (descriptor) 기능을 가지고 있으며, 이는 속성에 액세스하고 설정하는 방식을 제어할 수 있음을 의미합니다. 그러나 앞서 논의한 가져오기 문제를 해결하기 위해 이를 개선해야 합니다.

```bash
code validate.py
```

이러한 검증자 클래스를 살펴보면 검증 프로세스가 어떻게 작동하는지, 그리고 코드를 개선하기 위해 어떤 변경을 해야 하는지 더 잘 이해할 수 있습니다.
