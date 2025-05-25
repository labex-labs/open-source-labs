# 어서션 (Assertions)

`assert` 문은 프로그램의 내부 검사입니다. 표현식이 참이 아니면 `AssertionError` 예외를 발생시킵니다.

`assert` 문법:

```python
assert <expression> [, 'Diagnostic message']
```

예를 들어:

```python
assert isinstance(10, int), 'Expected int'
```

사용자 입력 (예: 웹 양식에 입력된 데이터 등) 을 확인하는 데 사용해서는 안 됩니다. 이는 내부 검사 및 불변성 (항상 참이어야 하는 조건) 을 위한 것입니다.
