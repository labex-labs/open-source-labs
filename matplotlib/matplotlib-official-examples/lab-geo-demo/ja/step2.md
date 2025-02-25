# グラフとサブプロットの作成

このステップでは、作成する各射影に対してグラフと4つのサブプロットを作成します。グラフとサブプロットを作成するには、`plt.subplots()` メソッドを使用します。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
