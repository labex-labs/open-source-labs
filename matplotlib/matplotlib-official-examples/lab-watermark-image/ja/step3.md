# プロットを作成する

これで、画像を重ねるプロットを作成できます。この例では、ランダムなデータを使用して単純な棒グラフを作成します。

```python
fig, ax = plt.subplots()

np.random.seed(19680801)
x = np.arange(30)
y = x + np.random.randn(30)
ax.bar(x, y, color='#6bbc6b')
ax.grid()
```
