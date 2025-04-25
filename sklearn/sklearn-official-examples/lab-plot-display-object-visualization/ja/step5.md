# 表示オブジェクトを単一のプロットに結合する

表示オブジェクトは、引数として渡された計算済みの値を格納します。これにより、Matplotlib の API を使用して視覚化を簡単に結合できます。次の例では、表示を 1 行に並べて配置します。

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```
