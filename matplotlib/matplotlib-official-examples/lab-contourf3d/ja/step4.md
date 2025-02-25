# コントアグラフを作成する

ここでは、`contourf()` メソッドを使ってコントアグラフを作成します。このメソッドは塗りつぶされたコントアを作成します。クール・ウォームカラーマップを使用するには、`cmap` パラメータを `cm.coolwarm` に設定します。

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
