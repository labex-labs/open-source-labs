# データセットの可視化

データセットをよりよく理解するために、matplotlibを使ってサンプル画像を可視化できます。次のコードは、データセットの最後の数字を表示します。

```python
import matplotlib.pyplot as plt

# Display the last digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```
