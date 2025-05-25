# 연습 문제 1.31: 오류 처리 (Error handling)

필드가 누락된 파일에서 함수를 시도하면 어떻게 될까요?

```python
>>> portfolio_cost('missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

이 시점에서 결정을 내려야 합니다. 프로그램을 작동시키려면 잘못된 줄을 제거하여 원래 입력 파일을 정리하거나, 일부 방식으로 잘못된 줄을 처리하도록 코드를 수정할 수 있습니다.

`pcost.py` 프로그램을 수정하여 예외를 포착하고, 경고 메시지를 인쇄한 다음 파일의 나머지 부분을 계속 처리하십시오.
