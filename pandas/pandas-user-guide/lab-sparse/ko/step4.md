# Sparse Accessor 사용

`.sparse` accessor 를 사용하여 희소 데이터에 특정한 속성 (attribute) 과 메서드 (method) 를 얻을 수 있습니다.

```python
# 희소 값을 가진 Series 생성
s = pd.Series([0, 0, 1, 2], dtype="Sparse[int]")

# sparse accessor 사용
print(s.sparse.density)
print(s.sparse.fill_value)
```
