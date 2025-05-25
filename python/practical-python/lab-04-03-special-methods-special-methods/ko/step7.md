# 속성 접근 (Attribute Access)

속성에 접근하고, 조작하며, 관리하는 다른 방법이 있습니다.

```python
getattr(obj, 'name')          # Same as obj.name
setattr(obj, 'name', value)   # Same as obj.name = value
delattr(obj, 'name')          # Same as del obj.name
hasattr(obj, 'name')          # Tests if attribute exists
```

예시:

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*참고: `getattr()`는 유용한 기본값 *arg\*도 가지고 있습니다.

```python
x = getattr(obj, 'x', None)
```
