# 예외 값 (Exception Values)

예외에는 연관된 값이 있습니다. 이 값은 무엇이 잘못되었는지에 대한 더 구체적인 정보를 포함합니다.

```python
raise RuntimeError('Invalid user name')
```

이 값은 `except`에 제공된 변수에 배치되는 예외 인스턴스의 일부입니다.

```python
try:
    ...
except RuntimeError as e:   # `e` holds the exception raised
    ...
```

`e`는 예외 유형의 인스턴스입니다. 그러나 인쇄될 때는 종종 문자열처럼 보입니다.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
