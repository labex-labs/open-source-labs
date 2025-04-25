# 将数据写入 Excel

你还可以使用`to_excel`方法将数据写入 Excel 文件。让我们将 DataFrame 保存到一个 Excel 文件中。

```python
# 将 DataFrame 保存到 Excel 文件
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
