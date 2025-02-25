# 密度の変化

このステップでは、密度を変化させた streamplot を作成します。`density` パラメータは、描画する流線の数を制御します。値が高いほど、流線が多くなります。

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
