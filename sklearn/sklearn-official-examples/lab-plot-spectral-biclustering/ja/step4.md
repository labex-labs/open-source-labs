# 結果のプロット

ここでは、`SpectralBiclustering`モデルによって割り当てられた行と列のラベルに基づいてデータを昇順に並べ替え、再度プロットします。`row_labels_`は 0 から 3 までの範囲で、`column_labels_`は 0 から 2 までの範囲で、各行には合計 4 つのクラスタがあり、各列には 3 つのクラスタがあります。

```python
# Reordering first the rows and then the columns.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")
_ = plt.show()
```

最後のステップとして、モデルによって割り当てられた行と列のラベルの関係を示したいと思います。そこで、`numpy.outer`を使ってグリッドを作成します。これは、ソートされた`row_labels_`と`column_labels_`を取り、各値に 1 を加えて、ラベルが 0 ではなく 1 から始まるようにして、より良い可視化を行います。

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Checkerboard structure of rearranged data")
plt.show()
```
