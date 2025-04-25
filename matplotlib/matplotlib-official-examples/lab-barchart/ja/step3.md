# グループ化された棒グラフを作成する

これで、Matplotlib の`bar`関数を使ってチャートを作成できます。属性をループして、それぞれに対して 1 セットの棒を作成するループを作成します。また、棒の幅と各セットの棒の位置を調整します。

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```
