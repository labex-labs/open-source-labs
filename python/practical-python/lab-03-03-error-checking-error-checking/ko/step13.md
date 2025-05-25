# `with` 문

최신 코드에서는 `try-finally` 문이 종종 `with` 문으로 대체됩니다.

```python
lock = Lock()
with lock:
    # lock acquired
    ...
# lock released
```

더 익숙한 예시:

```python
with open(filename) as f:
    # Use the file
    ...
# File closed
```

`with` 문은 리소스에 대한 사용 *컨텍스트*를 정의합니다. 실행이 해당 컨텍스트를 벗어나면 리소스가 해제됩니다. `with` 문은 이를 지원하도록 특별히 프로그래밍된 특정 객체에서만 작동합니다.
