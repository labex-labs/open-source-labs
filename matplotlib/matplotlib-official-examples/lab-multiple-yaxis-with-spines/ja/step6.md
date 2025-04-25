# 軸の範囲とラベルを設定する

`set` メソッドを使って各 y 軸の範囲とラベルを設定します。また、`set_color` メソッドを使って、ラベルの色を線の色と一致させます。

```python
ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
twin1.set(ylim=(0, 4), ylabel="Temperature")
twin2.set(ylim=(1, 65), ylabel="Velocity")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
```

ただし、このコードでは `twin2` が定義されていません。もし `twin2` が定義されていないままのまま翻訳すると、意味が通じなくなるので、もしかして `twin1` が 2 回登場しているのが間違いではないかと思われます。もしそうであれば、上記の翻訳は正しくなります。もし `twin2` が本来存在するものであれば、その定義が必要になります。
