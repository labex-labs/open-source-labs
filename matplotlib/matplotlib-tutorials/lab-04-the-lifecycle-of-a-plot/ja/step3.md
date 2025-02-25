# グラフを作成する

販売データを表すために棒グラフのビジュアライゼーションを使用します。以下の手順に従ってください。

1. `plt.subplots()` を使用して、グラフと軸オブジェクトを作成します。

```python
fig, ax = plt.subplots()
```

2. 軸オブジェクトの `barh()` メソッドを使用してデータをプロットします。

```python
ax.barh(group_names, group_data)
```
