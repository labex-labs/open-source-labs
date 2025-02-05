# 将 NumPy 数组保存为 Pillow 图像

既然我们已经有了 NumPy 数组，就可以将其传递给 Pillow，并以 Pillow 支持的任何格式保存。在这个例子中，我们将把绘图保存为 BMP 图像。

```python
im = Image.fromarray(rgba)
im.save("test.bmp")
```
