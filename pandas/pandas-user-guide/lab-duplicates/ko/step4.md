# 중복 레이블 감지

`Index.is_unique` 및 `Index.duplicated()` 메서드를 사용하여 중복 레이블을 확인할 수 있습니다.

```python
# Checking if the index has unique labels
print(df1.index.is_unique)

# Checking if the columns have unique labels
print(df1.columns.is_unique)

# Detecting duplicate labels in the index
print(df1.index.duplicated())
```
