# 加载数据集

在这一步中，我们将使用 `fetch_openml` 从 OpenML 加载泰坦尼克号数据集。

```python
X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
```
