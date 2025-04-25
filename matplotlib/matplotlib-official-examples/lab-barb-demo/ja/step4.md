# 風羽図のカスタマイズ

barbs 関数のパラメータを変更することで、風羽図をカスタマイズできます。たとえば、ベクトルの長さと支点を変更したり、空の風羽に対して円を塗りつぶしたり、旗と線の色を変更したりできます。

```python
plt.barbs(X, Y, U, V, length=8, pivot='middle', fill_empty=True, rounding=False,
          sizes=dict(emptybarb=0.25, spacing=0.2, height=0.3), flagcolor='r',
          barbcolor=['b', 'g'], flip_barb=True, barb_increments=dict(half=10, full=20, flag=100))
plt.show()
```
