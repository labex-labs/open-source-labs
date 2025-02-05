# 向绘图中添加表格

我们将使用`plt.table`函数在绘图的底部添加一个表格。我们会将单元格文本、行标签、行颜色和列标签作为参数传递给该函数。

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```
