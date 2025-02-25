# グーローシェーディング

`グーローシェーディング`も指定できます。この場合、四角形内の色はグリッド点間で線形補間されます。`X`、`Y`、`Z`の形状は同じでなければなりません。次のコードブロックを使用してグリッドを可視化できます。

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
