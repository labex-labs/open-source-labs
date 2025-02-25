# データを Excel に書き込む

`to_excel` メソッドを使用して、データを Excel ファイルに書き込むこともできます。DataFrame を Excel ファイルに保存しましょう。

```python
# Saving DataFrame to an Excel file
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
