# 途切れない流線

このステップでは、途切れない流線を持つ streamplot を作成します。`broken_streamlines` パラメータは、単一のグリッドセル内の線の数の制限を超えた場合に流線を途切るかどうかを制御します。

```python
plt.streamplot(X, Y, U, V, broken_streamlines=False)
plt.title('Streamplot with Unbroken Streamlines')
plt.show()
```
