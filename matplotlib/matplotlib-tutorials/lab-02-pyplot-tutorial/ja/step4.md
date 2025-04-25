# カテゴリ変数を使った描画

Matplotlib を使えば、カテゴリ変数を使ってグラフを作成できます。カテゴリ変数を使って棒グラフ、散布図、折れ線グラフを作成しましょう。

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)

plt.suptitle('Categorical Plotting')
plt.show()
```

解説：

- 3 つのカテゴリ値を持つリスト `names` と、それに対応する値を表すリスト `values` を作成します。
- `figure` 関数を呼び出して、指定されたサイズの新しいグラフを作成します。
- `subplot` 関数を使ってサブプロットのグリッドを作成します。この例では、3 つのサブプロットを作成し、それぞれ異なる種類のグラフ（棒グラフ、散布図、折れ線グラフ）を描画します。
- `suptitle` 関数を使って、グラフの上位タイトルを設定します。
