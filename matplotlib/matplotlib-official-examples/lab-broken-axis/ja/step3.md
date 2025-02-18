# サブプロットを作成する

次に、2 つのサブプロットを作成します。1 つは外れ値（outlier）用、もう 1 つは大部分のデータ用です。`plt.subplots` を使用してサブプロットを作成し、`sharex` パラメータを `True` に設定することで、同じ x 軸を共有するようにします。

```python
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
```
