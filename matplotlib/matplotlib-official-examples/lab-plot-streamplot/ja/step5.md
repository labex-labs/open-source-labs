# 線幅の変化

このステップでは、線幅を変化させた streamplot を作成します。`linewidth` パラメータは、流線の幅を制御します。ここでは、先ほど計算した `speed` 配列を使って線幅を変化させています。

```python
lw = 5*speed / speed.max()
plt.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)
plt.title('Varying Line Width')
plt.show()
```
