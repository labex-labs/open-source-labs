# 빈 딕셔너리 테스트 (예외 케이스)

빈 딕셔너리 케이스에 대한 테스트를 추가해 보겠습니다. `test_key_of_max.py`의 `TestKeyOfMax` 클래스에 이 메서드를 추가합니다.

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`**: 이 어설션은 값이 특히 `None`인지 확인합니다. `self.assertEqual(..., None)`은 `None`으로 *평가*되지만 실제로 `None`이 아닌 것에 대해 통과할 수 있기 때문에 중요합니다. `assertIsNone`은 더 엄격합니다.

테스트를 다시 실행합니다 (`python3 test_key_of_max.py`). 이제 세 개의 테스트 (두 개의 기본 테스트와 빈 딕셔너리 테스트) 가 모두 통과해야 합니다.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
