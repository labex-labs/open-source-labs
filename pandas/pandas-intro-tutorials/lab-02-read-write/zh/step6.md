# 从 Excel 读取数据

从 Excel 文件读取数据就像从 CSV 文件读取数据一样简单。我们将使用 pandas 的`read_excel`函数。

```python
# 从 Excel 文件读取数据
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
