# 単純なエラーバープロットを作成する

`errorbar`関数を使って、標準エラーバー付きの単純なエラーバープロットを作成します。ここでは、x値とy値とそれに対応する誤差値を設定します。また、線のスタイルを点線に設定します。

```python
fig, ax = plt.subplots(figsize=(7, 4))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
