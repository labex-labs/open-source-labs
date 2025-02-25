# データフレームを作成する

pandas のデータはデータフレームに格納されます。これは、列が異なる型である可能性のある 2 次元のラベル付きデータ構造です。

```python
# Creating a DataFrame
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
```
