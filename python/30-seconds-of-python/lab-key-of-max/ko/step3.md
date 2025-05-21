# 유닛 테스트 생성: 기본 테스트

이제 함수가 올바르게 작동하는지 확인하기 위해 몇 가지 테스트를 작성해 보겠습니다. Python 의 `unittest` 모듈을 사용합니다. `test_key_of_max.py`라는 새 파일을 생성하고 다음 코드를 추가합니다.

```python
import unittest
from key_of_max import key_of_max  # 함수 가져오기

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

설명:

1.  **`import unittest`**: 테스트 프레임워크를 가져옵니다.
2.  **`from key_of_max import key_of_max`**: 테스트하려는 함수를 가져옵니다.
3.  **`class TestKeyOfMax(unittest.TestCase):`**: *테스트 클래스*를 정의합니다. 테스트 클래스는 관련된 테스트를 함께 그룹화합니다.
4.  **`def test_basic_case(self):`**: *테스트 메서드*를 정의합니다. 각 테스트 메서드는 함수의 특정 측면을 확인합니다. 테스트 메서드 이름은 `test_`로 시작해야 합니다.
5.  **`self.assertEqual(...)`**: 이것은 *어설션 (assertion)*입니다. 두 값이 같은지 확인합니다. 같지 않으면 테스트가 실패합니다. 이 경우 `key_of_max({'a': 4, 'b': 0, 'c': 13})`이 `'c'`를 반환하는지 확인하고 있습니다.
6.  **`def test_another_case(self):`**: 최대 값의 키가 고유하지 않을 수 있는지 확인하기 위해 다른 테스트 케이스를 추가했습니다.
7.  **`if __name__ == '__main__': unittest.main()`**: 이 표준 Python 관용구는 스크립트를 직접 실행할 때 (예: `python3 test_key_of_max.py`) 테스트를 실행합니다.

터미널에서 테스트를 실행합니다: `python3 test_key_of_max.py`. 두 테스트가 통과했음을 나타내는 출력이 표시되어야 합니다.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
