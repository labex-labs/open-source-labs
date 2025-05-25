# 오류와 예외 (Errors and exceptions)

함수는 오류를 예외 (exception) 로 보고합니다. 예외는 함수가 중단되도록 하며, 처리되지 않은 경우 전체 프로그램이 중지될 수 있습니다.

Python REPL 에서 다음을 시도해 보십시오.

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

디버깅 목적으로, 메시지는 무슨 일이 발생했는지, 오류가 어디에서 발생했는지, 그리고 실패로 이어진 다른 함수 호출을 보여주는 추적 (traceback) 을 설명합니다.
