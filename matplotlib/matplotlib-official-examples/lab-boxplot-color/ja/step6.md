# 水平グリッド線の追加

最後に、`yaxis.grid()`関数を使ってボックスプロットに水平グリッド線を追加します。

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three Separate Samples')
    ax.set_ylabel('Observed Values')

plt.show()
```
