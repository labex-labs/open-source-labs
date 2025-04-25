# 2 つのサブプロット付きのグラフを作成する

まず、2 つのサブプロット付きのグラフを作成する必要があります。2 つのサブプロットを横並びに配置したグラフを作成するには、`plt.subplots()` メソッドを使用します。

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
