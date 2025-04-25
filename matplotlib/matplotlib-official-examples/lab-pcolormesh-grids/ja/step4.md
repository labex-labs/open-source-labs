# フラットシェーディング、同じ形状のグリッド

グリッドが各次元のデータと同じ形状の場合、`shading='flat'`を使用することはできません。歴史的に、Matplotlib はこの場合、Matlab の動作に合わせて、`Z`の最後の行と列を無視してしまいました。この動作が依然として望まれる場合は、最後の行と列を手動で削除してください。次のコードブロックを使用してグリッドを可視化できます。

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
