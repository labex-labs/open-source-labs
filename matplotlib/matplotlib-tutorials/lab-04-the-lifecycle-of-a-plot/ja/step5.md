# グラフの外観をカスタマイズする

グラフの外観をさらにカスタマイズすることができます。以下の手順に従ってください。

1. x 軸のラベルを回転させて、読みやすくします。

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. x 軸と y 軸の範囲、ラベル、タイトルを設定します。

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. もう一度グラフを表示します。

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
