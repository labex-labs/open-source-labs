# 항목 접근을 위한 특수 메서드

이들은 컨테이너를 구현하기 위한 메서드입니다.

```python
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)
```

클래스에서 사용할 수 있습니다.

```python
class Sequence:
    def __len__(self):
        ...
    def __getitem__(self,a):
        ...
    def __setitem__(self,a,v):
        ...
    def __delitem__(self,a):
        ...
```
