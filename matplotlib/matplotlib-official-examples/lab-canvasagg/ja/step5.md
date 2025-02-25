# numpy配列をPillow画像に保存する

numpy配列ができたので、それをPillowに渡して、Pillowがサポートする任意の形式で保存することができます。この例では、グラフをBMP画像として保存します。

```python
im = Image.fromarray(rgba)
im.save("test.bmp")
```
