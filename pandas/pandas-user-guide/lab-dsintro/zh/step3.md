# 创建一个 DataFrame

另一个基本数据结构是 DataFrame。它是一个二维带标签的数据结构，其列的数据类型可能不同。

```python
# 创建一个 DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
