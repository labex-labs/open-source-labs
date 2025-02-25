# 最初のページを作成する

このステップでは、PDFファイルの最初のページを作成します。このページには、単純なグラフのプロットが含まれます。

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
