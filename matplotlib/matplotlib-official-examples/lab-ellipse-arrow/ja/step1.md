# Matplotlib をインポートしてグラフと軸を作成する

まず、Matplotlib をインポートしてグラフと軸を作成する必要があります。グラフと軸は、プロットのコンテナです。

```python
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```
