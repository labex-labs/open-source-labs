# 目盛りの色を設定する

各y軸の目盛りの色をラベルの色と一致させます。

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```

ただし、このコードでは `twin2` が定義されていません。もし `twin2` が定義されていないままのまま翻訳すると、意味が通じなくなるので、もしかして `twin1` が2回登場しているのが間違いではないかと思われます。もしそうであれば、上記の翻訳は正しくなります。もし `twin2` が本来存在するものであれば、その定義が必要になります。
