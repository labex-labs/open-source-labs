# 列ラベルを小文字に変換する

最後に、関数を使って列ラベルを小文字に変換します。

```python
# Convert column labels to lowercase
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
```
