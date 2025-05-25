# 모든 오류 잡기 (Catching All Errors)

모든 예외를 잡으려면 다음과 같이 `Exception`을 사용하십시오.

```python
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
```

일반적으로, 이와 같은 코드를 작성하는 것은 좋지 않은 생각입니다. 왜 실패했는지 알 수 없기 때문입니다.
