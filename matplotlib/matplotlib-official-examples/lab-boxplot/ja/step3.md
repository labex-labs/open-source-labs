# デフォルトのボックスプロット

まずは、データを視覚化するためのデフォルトのボックスプロットを作成します。Matplotlib の関数 `boxplot()` を使って、データとラベルを引数として渡します。また、`set_title()` 関数を使ってプロットのタイトルを設定します。

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```
