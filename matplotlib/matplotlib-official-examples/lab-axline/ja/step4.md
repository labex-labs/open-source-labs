# 対角線を描画する

固定された傾きの対角線を描画するために、`transform`パラメータを持つ`axline`を使用することができます。固定された傾き`0.5`の対角線グリッド線を描画してみましょう。

```python
import matplotlib.pyplot as plt
import numpy as np

# Draw diagonal lines
for pos in np.linspace(-2, 1, 10):
    plt.axline((pos, 0), slope=0.5, color='k', transform=plt.gca().transAxes)

plt.ylim([0, 1])
plt.xlim([0, 1])
plt.show()
```
