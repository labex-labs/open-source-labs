# 모든 음수 값으로 테스트

마지막 테스트로, 딕셔너리의 모든 값이 음수인 경우를 처리해 보겠습니다. `TestKeyOfMax`에 이 메서드를 추가합니다.

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

이 테스트는 함수가 _가장 작은 음수_ 값 (이 경우 최대값) 을 올바르게 식별하고 관련 키를 반환하는지 확인합니다.

마지막으로 테스트를 실행합니다 (`python3 test_key_of_max.py`). 네 개의 테스트가 모두 통과해야 합니다. 이를 통해 함수가 올바르게 작동한다는 높은 신뢰도를 얻을 수 있습니다.

완전한 `test_key_of_max.py`는 이제 다음과 같아야 합니다.

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```

테스트를 다시 실행합니다 (`python3 test_key_of_max.py`). 네 개의 테스트가 모두 통과해야 합니다. 이를 통해 함수가 올바르게 작동한다는 높은 신뢰도를 얻을 수 있습니다.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
