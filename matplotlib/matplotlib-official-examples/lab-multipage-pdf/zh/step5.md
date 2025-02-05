# 创建第三页

在这一步中，你将创建 PDF 文件的第三页。该页面将包含一条抛物线的图表。

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # 或者你可以将一个 Figure 对象传递给 pdf.savefig
plt.close()
```
