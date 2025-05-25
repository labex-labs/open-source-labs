# 예외 발생시키기 (Raising Exceptions)

예외를 발생시키려면 `raise` 문을 사용하십시오.

```python
raise RuntimeError('What a kerfuffle')
```

이렇게 하면 `try-except` 블록에 의해 포착되지 않는 한, 프로그램이 예외 추적과 함께 중단됩니다.

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
