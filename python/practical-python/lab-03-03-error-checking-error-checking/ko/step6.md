# 여러 오류 잡기 (Catching Multiple Errors)

여러 개의 `except` 블록을 사용하여 다양한 종류의 예외를 잡을 수 있습니다.

```python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

또는, 이를 처리하는 문장이 동일한 경우, 그룹화할 수 있습니다.

```python
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
```
