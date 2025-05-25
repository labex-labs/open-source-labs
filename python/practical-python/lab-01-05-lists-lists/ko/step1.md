# 리스트 생성

리스트 리터럴 (list literal) 을 정의하려면 대괄호를 사용합니다.

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]
nums = [ 39, 38, 42, 65, 111]
```

때로는 다른 방법으로 리스트가 생성됩니다. 예를 들어, 문자열은 `split()` 메서드를 사용하여 리스트로 분할될 수 있습니다.

```python
>>> line = 'GOOG,100,490.10'
>>> row = line.split(',')
>>> row
['GOOG', '100', '490.10']
>>>
```
