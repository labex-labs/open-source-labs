# プロットをカスタマイズする

このステップでは、`bottom`パラメータを使ってベースラインを変更し、`linefmt`、`markerfmt`、`basefmt`パラメータを使って形式を変更することで、3Dのステムプロットをカスタマイズします。

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(
    x, y, z, linefmt='grey', markerfmt='D', bottom=np.pi)
markerline.set_markerfacecolor('none')

plt.show()
```
