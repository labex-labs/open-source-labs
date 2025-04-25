# 積分のラベルを追加する

`text`を使ってグラフに積分のラベルを追加します。ラベルは a と b の中点に中央揃えにし、mathtext を使ってフォーマットする必要があります。

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
