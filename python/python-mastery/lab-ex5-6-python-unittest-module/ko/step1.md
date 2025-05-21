# 첫 번째 유닛 테스트 생성하기

Python 의 `unittest` 모듈은 테스트를 구성하고 실행하는 구조화된 방법을 제공하는 강력한 도구입니다. 첫 번째 유닛 테스트를 작성하기 전에 몇 가지 핵심 개념을 이해해 보겠습니다. 테스트 픽스처 (test fixture) 는 테스트 전에 환경을 준비하고 테스트 후에 정리하는 데 도움이 되는 `setUp` 및 `tearDown`과 같은 메서드입니다. 테스트 케이스 (test case) 는 개별 테스트 단위이고, 테스트 스위트 (test suite) 는 테스트 케이스의 모음이며, 테스트 러너 (test runner) 는 이러한 테스트를 실행하고 결과를 표시하는 역할을 합니다.

이 첫 번째 단계에서는 `stock.py` 파일에 이미 정의된 `Stock` 클래스에 대한 기본 테스트 파일을 생성할 것입니다.

1. 먼저, `stock.py` 파일을 엽니다. 이렇게 하면 테스트할 `Stock` 클래스를 이해하는 데 도움이 됩니다. `stock.py`의 코드를 보면 클래스가 어떻게 구성되어 있는지, 어떤 속성을 가지고 있는지, 어떤 메서드를 제공하는지 알 수 있습니다. `stock.py` 파일의 내용을 보려면 터미널에서 다음 명령을 실행하십시오.

```bash
cat stock.py
```

2. 이제 선호하는 텍스트 편집기를 사용하여 `teststock.py`라는 새 파일을 생성할 차례입니다. 이 파일에는 `Stock` 클래스에 대한 테스트 케이스가 포함됩니다. 다음은 `teststock.py` 파일에 작성해야 하는 코드입니다.

```python
# teststock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

이 코드의 주요 구성 요소를 살펴보겠습니다.

- `import unittest`: 이 줄은 Python 에서 테스트를 작성하고 실행하는 데 필요한 도구와 클래스를 제공하는 `unittest` 모듈을 가져옵니다.
- `import stock`: `Stock` 클래스를 포함하는 모듈을 가져옵니다. 이 import 가 없으면 테스트 코드에서 `Stock` 클래스에 액세스할 수 없습니다.
- `class TestStock(unittest.TestCase)`: `unittest.TestCase`에서 상속받는 `TestStock`라는 새 클래스를 생성합니다. 이렇게 하면 `TestStock` 클래스가 여러 테스트 메서드를 포함할 수 있는 테스트 케이스 클래스가 됩니다.
- `def test_create(self)`: 이것은 테스트 메서드입니다. `unittest` 프레임워크에서 모든 테스트 메서드는 `test_` 접두사로 시작해야 합니다. 이 메서드는 `Stock` 클래스의 인스턴스를 생성한 다음 `assertEqual` 메서드를 사용하여 `Stock` 인스턴스의 속성이 예상 값과 일치하는지 확인합니다.
- `assertEqual`: 이것은 `TestCase` 클래스에서 제공하는 메서드입니다. 두 값이 같은지 확인합니다. 같지 않으면 테스트가 실패합니다.
- `unittest.main()`: 이 스크립트가 직접 실행되면 `unittest.main()`은 `TestStock` 클래스의 모든 테스트 메서드를 실행하고 결과를 표시합니다.

3. `teststock.py` 파일에 코드를 작성한 후 저장합니다. 그런 다음 터미널에서 다음 명령을 실행하여 테스트를 실행합니다.

```bash
python3 teststock.py
```

다음과 유사한 출력이 표시됩니다.

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

출력의 단일 점 (`.`) 은 하나의 테스트가 성공적으로 통과했음을 나타냅니다. 테스트가 실패하면 점 대신 `F`가 표시되며 테스트에서 무엇이 잘못되었는지에 대한 자세한 정보가 함께 제공됩니다. 이 출력은 코드가 예상대로 작동하는지 또는 수정해야 할 문제가 있는지 빠르게 식별하는 데 도움이 됩니다.
