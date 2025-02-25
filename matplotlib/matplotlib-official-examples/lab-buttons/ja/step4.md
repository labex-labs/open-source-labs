# `Next`と`Previous`のボタンを作成する

次に、`matplotlib.pyplot`の`add_axes`関数を使って`Next`と`Previous`のボタンを作成し、先ほど作成したコールバック関数を`on_clicked`を使って割り当てます。

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
