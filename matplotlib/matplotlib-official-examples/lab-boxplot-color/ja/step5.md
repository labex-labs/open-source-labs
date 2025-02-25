# カスタムカラーでボックスプロットを塗りつぶす

次に、カスタムカラーでボックスプロットを塗りつぶします。色のリストを作成し、ループを使って各ボックスを異なる色で塗りつぶします。

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
