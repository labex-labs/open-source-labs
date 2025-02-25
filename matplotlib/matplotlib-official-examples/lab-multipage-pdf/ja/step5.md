# 3番目のページを作成する

このステップでは、PDFファイルの3番目のページを作成します。このページには、放物線のプロットが含まれます。

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
plt.close()
```
