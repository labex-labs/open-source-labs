# 예외 다시 발생시키기 (Reraising an Exception)

잡힌 오류를 전파하려면 `raise`를 사용하십시오.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

이를 통해 조치를 취하고 (예: 로깅) 오류를 호출자에게 전달할 수 있습니다.
