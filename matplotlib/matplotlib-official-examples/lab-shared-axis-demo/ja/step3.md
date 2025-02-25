# サブプロットを作成する

`plt.subplot()` メソッドを使ってサブプロットを作成できます。この例では、最初のサブプロットが 1 行目と 3 列目を占め、2 番目と 3 番目のサブプロットがそれぞれ 2 行目と 3 行目を占め、1 番目のサブプロットと x 軸を共有する 3 つのサブプロットを作成します。

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```
