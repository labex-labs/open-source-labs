# スタイルサイクルを設定する

`cycler` を使ってヒストグラム用のスタイルサイクルを設定します。3 つのスタイルサイクルを作成します。1 つは面の色用、1 つはラベル用、1 つはハッチパターン用です。

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```
