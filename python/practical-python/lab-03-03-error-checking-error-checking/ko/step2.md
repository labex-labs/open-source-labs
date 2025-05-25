# 예외 (Exceptions)

예외는 오류를 알리는 데 사용됩니다. 예외를 직접 발생시키려면 `raise` 문을 사용합니다.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

예외를 잡으려면 `try-except`를 사용합니다.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
