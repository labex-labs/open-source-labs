# 리스트 제거

요소 값 또는 인덱스를 사용하여 항목을 제거할 수 있습니다.

```python
# Using the value
names.remove('Curtis')

# Using the index
del names[1]
```

항목을 제거해도 구멍이 생기지 않습니다. 다른 항목은 비워진 공간을 채우기 위해 아래로 이동합니다. 요소가 두 번 이상 나타나는 경우, `remove()`는 첫 번째 발생만 제거합니다.
