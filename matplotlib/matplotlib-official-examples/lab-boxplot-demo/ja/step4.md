# ボックスプロットをカスタマイズする

ボックス、ひげ、外れ値の外観を変更することで、ボックスプロットをカスタマイズできます。また、同じプロットに複数のボックスプロットを作成して、異なるグループのデータを比較することもできます。以下は、ボックスプロットをカスタマイズする方法のいくつかの例です。

```python
# ノッチ付きのボックスプロットを作成する
plt.boxplot(data, notch=True)
plt.show()

# 外れ値の点のシンボルを緑のダイヤモンドに変更する
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# 水平方向のボックスプロットを作成する
plt.boxplot(data, vert=False)
plt.show()

# 1 つのプロットに複数のボックスプロットを作成する
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
