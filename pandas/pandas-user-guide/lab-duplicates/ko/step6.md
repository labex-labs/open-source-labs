# 중복 레이블 플래그 확인 및 설정

마지막으로, DataFrame 에서 `allows_duplicate_labels` 플래그를 확인하고 설정할 수 있습니다.

```python
# Creating a DataFrame and setting allows_duplicate_labels to False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# Checking the allows_duplicate_labels flag
print(df.flags.allows_duplicate_labels)

# Setting allows_duplicate_labels to True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
