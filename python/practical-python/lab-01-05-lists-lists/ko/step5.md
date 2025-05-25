# 리스트 정렬

리스트는 "제자리에서 (in-place)" 정렬될 수 있습니다.

```python
s = [10, 1, 7, 3]
s.sort()                    # [1, 3, 7, 10]

# Reverse order
s = [10, 1, 7, 3]
s.sort(reverse=True)        # [10, 7, 3, 1]

# It works with any ordered data
s = ['foo', 'bar', 'spam']
s.sort()                    # ['bar', 'foo', 'spam']
```

새로운 리스트를 만들고 싶다면 `sorted()`를 사용하십시오:

```python
t = sorted(s)               # s unchanged, t holds sorted values
```
