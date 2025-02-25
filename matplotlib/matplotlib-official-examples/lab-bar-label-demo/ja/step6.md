# コール可能オブジェクトを使用した棒グラフのラベリング

最後に、コール可能オブジェクトを使用して棒グラフのラベルを書式設定する方法を示します。異なる動物の走行速度に関するいくつかのデータを使用します。

```python
animal_names = ['Lion', 'Gazelle', 'Cheetah']
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()
bar_container = ax.bar(animal_names, mph_speed)
ax.set(ylabel='speed in MPH', title='Running speeds', ylim=(0, 80))
ax.bar_label(bar_container, fmt=lambda x: f'{x * 1.61:.1f} km/h')
```
