# 色の変化

このステップでは、色を変化させた streamplot を作成します。`color` パラメータは、ベクトルフィールドの大きさを表す 2 次元配列をとります。ここでは、ベクトルフィールドの `U` 成分を色として使用しています。

```python
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')
plt.colorbar(strm.lines)
plt.title('Varying Color')
plt.show()
```
