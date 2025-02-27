# 結果をプロットする

最後に、画像上に結果をプロットすることができます。リサイズされた画像とクラスタの輪郭をプロットするためにmatplotlibを使います。各クラスタをループして、そのクラスタ内の画素の輪郭をプロットします。

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(
        label == l,
        colors=[
            plt.cm.nipy_spectral(l / float(n_clusters)),
        ],
    )
plt.axis("off")
plt.show()
```
