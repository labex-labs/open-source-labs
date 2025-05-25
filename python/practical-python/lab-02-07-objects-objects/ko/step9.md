# 타입 검사 (Type Checking)

객체가 특정 타입인지 확인하는 방법.

```python
if isinstance(a, list):
    print('a is a list')
```

여러 가능한 타입 중 하나를 확인하는 방법.

```python
if isinstance(a, (list,tuple)):
    print('a is a list or tuple')
```

\*주의: 타입 검사를 과도하게 사용하지 마십시오. 이는 과도한 코드 복잡성을 초래할 수 있습니다. 일반적으로, 다른 사용자가 코드를 사용할 때 흔히 저지르는 실수를 방지할 수 있는 경우에만 수행하는 것이 좋습니다.
