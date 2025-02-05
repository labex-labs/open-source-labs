# 将数据写入Excel

你还可以使用`to_excel`方法将数据写入Excel文件。让我们将DataFrame保存到一个Excel文件中。

```python
# 将DataFrame保存到Excel文件
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
