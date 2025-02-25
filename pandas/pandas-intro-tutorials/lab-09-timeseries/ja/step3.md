# 測定月の新しい列を追加する

今、DataFrameに、各測定の月のみを含む新しい列を追加したいと思います。これは、`dt` アクセサを使って達成できます。

```python
# 各測定の月の新しい列を追加する
air_quality["month"] = air_quality["datetime"].dt.month
```
