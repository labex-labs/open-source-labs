# Matplotlib をインポートして散布図を作成する

まずは Matplotlib をインポートして散布図を作成します。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```
