# 깊은 복사 (Deep copies)

때로는 객체와 그 안에 포함된 모든 객체의 복사본을 만들어야 할 필요가 있습니다. 이를 위해 `copy` 모듈을 사용할 수 있습니다.

```python
>>> a = [2,3,[100,101],4]
>>> import copy
>>> b = copy.deepcopy(a)
>>> a[2].append(102)
>>> b[2]
[100,101]
>>> a[2] is b[2]
False
>>>
```
