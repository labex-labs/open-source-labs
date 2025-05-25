# DataFrame 열 조작

DataFrame 열에 대해 다양한 작업을 수행할 수 있습니다. 예를 들어, 열을 선택하고, 새 열을 추가하거나, 열을 삭제할 수 있습니다.

```python
# Select column A
df['A']

# Add a new column E
df['E'] = pd.Series(np.random.randn(6), index=df.index)

# Delete column B
del df['B']
```
