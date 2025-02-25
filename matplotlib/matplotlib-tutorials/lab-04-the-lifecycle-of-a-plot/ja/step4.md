# グラフのスタイルをカスタマイズする

グラフのスタイルを変更して、視覚的に魅力的にすることができます。以下の手順に従ってください。

1. `print(plt.style.available)` を使用して、利用可能なスタイルのリストを表示します。

```python
print(plt.style.available)
```

2. スタイルを選択して、`plt.style.use(style_name)` を使用して適用します。

```python
plt.style.use('fivethirtyeight')
```

3. もう一度グラフを表示しましょう。

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```
