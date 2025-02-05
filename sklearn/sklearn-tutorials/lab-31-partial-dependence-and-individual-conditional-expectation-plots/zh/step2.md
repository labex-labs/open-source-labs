# 加载并准备数据

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# 创建一个DataFrame以便于数据操作
df = pd.DataFrame(X, columns=feature_names)
```
