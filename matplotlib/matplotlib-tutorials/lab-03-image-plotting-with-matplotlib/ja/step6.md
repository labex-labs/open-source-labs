# 配列補間スキーム

画像のサイズ変更時には、欠けた領域を埋めるために画素値を補間する必要があります。異なる補間スキームを使って、画素の周囲の画素に基づいて画素値を決定することができます。Matplotlib は、「nearest」、「bilinear」、「bicubic」などの異なる補間オプションを提供しています。

```python
plt.imshow(img, interpolation="bilinear")
```
