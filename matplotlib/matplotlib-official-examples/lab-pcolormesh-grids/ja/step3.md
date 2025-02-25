# フラットシェーディング

Matplotlibの`pcolormesh`関数は、2次元グリッドを可視化できます。最も少ない仮定でグリッドを指定するのは`shading='flat'`であり、グリッドが各次元のデータよりも1つ大きい場合、つまり形状が`(M+1, N+1)`の場合です。その場合、`X`と`Y`は、`Z`の値で塗りつぶされる四角形の角を指定します。次のコードブロックを使用してグリッドを可視化できます。

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
