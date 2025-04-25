# 異なるスケールパラメータ「linear_width」の「asinh」グラフを比較する

ここでは、異なるスケールパラメータ「linear_width」の「asinh」グラフを比較します。異なる「linear_width」値の 3 つのグラフをプロットします。

```python
fig2 = plt.figure(layout='constrained')
axs = fig2.subplots(1, 3, sharex=True)
for ax, (a0, base) in zip(axs, ((0.2, 2), (1.0, 0), (5.0, 10))):
    ax.set_title(f'linear_width={a0:.3g}')
    ax.plot(x, x, label='y=x')
    ax.plot(x, 10*x, label='y=10x')
    ax.plot(x, 100*x, label='y=100x')
    ax.set_yscale('asinh', linear_width=a0, base=base)
    ax.grid()
    ax.legend(loc='best', fontsize='small')
```
