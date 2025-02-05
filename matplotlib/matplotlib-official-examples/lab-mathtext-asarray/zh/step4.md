# 使用像素坐标定位将文本绘制到图形上

或者，我们可以通过将 `.Figure.text` 与 `.transforms.IdentityTransform` 一起使用，直接在图形上以像素坐标定位来绘制文本。

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
