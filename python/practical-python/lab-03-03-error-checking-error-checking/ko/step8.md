# 오류를 잡는 잘못된 방법 (Wrong Way to Catch Errors)

다음은 예외를 사용하는 잘못된 방법입니다.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

이것은 가능한 모든 오류를 잡으며, 전혀 예상하지 못한 이유 (예: 설치되지 않은 Python 모듈 등) 로 인해 코드가 실패할 때 디버깅을 불가능하게 만들 수 있습니다.
