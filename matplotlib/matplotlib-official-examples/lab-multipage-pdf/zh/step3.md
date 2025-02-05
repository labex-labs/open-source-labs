# 创建第一页

在这一步中，你将创建 PDF 文件的第一页。该页面将包含一个简单图形的图表。

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
