# 複数のビジュアライゼーションを組み合わせる

ビジュアライゼーションに追加のグラフ要素を追加することができます。以下の手順に従ってください。

1. 販売データの平均を表す垂直線を追加します。

```python
ax.axvline(group_mean, ls='--', color='r')
```

2. グラフに新しい会社を注釈付きで追加します。

```python
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")
```

3. グラフのタイトルの位置を調整します。

```python
ax.title.set(y=1.05)
```

4. 完全なコードを以下に示します。

```python
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')

plt.show()
```
