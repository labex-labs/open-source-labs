# 얕은 복사 (Shallow copies)

리스트와 딕셔너리에는 복사 방법이 있습니다.

```python
>>> a = [2,3,[100,101],4]
>>> b = list(a) # Make a copy
>>> a is b
False
```

새로운 리스트이지만, 리스트 항목은 공유됩니다.

```python
>>> a[2].append(102)
>>> b[2]
[100,101,102]
>>>
>>> a[2] is b[2]
True
>>>
```

예를 들어, 내부 리스트 `[100, 101, 102]`가 공유되고 있습니다. 이것을 얕은 복사라고 합니다. 다음은 그림입니다.

![Shallow copy](../assets/shallow.png)
