# 다소 나은 접근 방식 (Somewhat Better Approach)

모든 오류를 잡으려는 경우, 이것이 더 합리적인 접근 방식입니다.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
```

이는 실패에 대한 구체적인 이유를 보고합니다. 가능한 모든 예외를 잡는 코드를 작성할 때는 오류를 보고/확인할 수 있는 메커니즘을 갖는 것이 거의 항상 좋은 생각입니다.

하지만 일반적으로, 합리적인 범위 내에서 오류를 좁게 잡는 것이 더 좋습니다. 실제로 처리할 수 있는 오류만 잡으십시오. 다른 오류는 지나가게 하십시오. 아마 다른 코드가 처리할 수 있을 것입니다.
