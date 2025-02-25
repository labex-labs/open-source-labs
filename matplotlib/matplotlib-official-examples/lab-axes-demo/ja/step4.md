# インセット軸を作成する

このステップでは、`fig.add_axes`を使ってメインプロット軸内に2つのインセット軸を作成します。1つはデータのヒストグラムを表示し、もう1つはインパルス応答を表示します。

```python
# Create right inset axes
right_inset_ax = fig.add_axes([.65,.6,.2,.2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probability', xticks=[], yticks=[])

# Create left inset axes
left_inset_ax = fig.add_axes([.2,.6,.2,.2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Impulse response', xlim=(0,.2), xticks=[], yticks=[])
```
