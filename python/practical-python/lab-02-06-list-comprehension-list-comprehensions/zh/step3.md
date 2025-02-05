# 用例

列表推导式非常有用。例如，你可以收集特定字典字段的值：

```python
stocknames = [s['name'] for s in stocks]
```

你可以对序列执行类似数据库的查询。

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

你还可以将列表推导式与序列归约相结合：

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```
