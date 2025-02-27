# 密度推定を可視化する

最後に、ヒストグラムと推定された密度関数を使って密度推定を可視化できます。元のデータのヒストグラムと推定された密度関数をプロットすることができます。

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```
