# 最寄りシェーディング、同じ形状のグリッド

通常、ユーザーが`X`、`Y`、`Z`をすべて同じ形状にするときに、1 行と 1 列のデータを削除することは意図していません。この場合、Matplotlib は`shading='nearest'`を許可し、塗りつぶされた四角形をグリッド点の中心に配置します。`shading='nearest'`で正しい形状でないグリッドが渡された場合、エラーが発生します。次のコードブロックを使用してグリッドを可視化できます。

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
