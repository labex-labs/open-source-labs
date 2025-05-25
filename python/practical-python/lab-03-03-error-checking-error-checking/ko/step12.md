# `finally` 문

예외 발생 여부에 관계없이 실행되어야 하는 코드를 지정합니다.

```python
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.
```

일반적으로 리소스 (특히 락, 파일 등) 를 안전하게 관리하는 데 사용됩니다.
