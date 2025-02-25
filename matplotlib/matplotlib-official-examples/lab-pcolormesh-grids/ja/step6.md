# 自動シェーディング

ユーザーがコードによって自動的に使用するものを選択して欲しい場合があります。この場合、`shading='auto'`は`X`、`Y`、および`Z`の形状に基づいて`flat`または`nearest`シェーディングを使用するかどうかを決定します。次のコードブロックを使用してグリッドを可視化できます。

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```
