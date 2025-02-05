# 从Excel读取数据

从Excel文件读取数据就像从CSV文件读取数据一样简单。我们将使用pandas的`read_excel`函数。

```python
# 从Excel文件读取数据
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
