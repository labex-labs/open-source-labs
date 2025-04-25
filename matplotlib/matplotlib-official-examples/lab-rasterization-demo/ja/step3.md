# 4 つのサブプロット付きのグラフを作成する

ラスタライズのさまざまな側面を示すために、4 つのサブプロット付きのグラフを作成します。

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
