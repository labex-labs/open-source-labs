# 小目盛りラベルを整列させる

最後に、小目盛りラベルを大目盛りの間の中央に整列させる必要があります。これは`get_xticklabels()`関数を使って、小目盛りラベルを取得するために`minor`パラメータを`True`に設定することで行えます。その後、ラベルをループして水平整列を`'center'`に設定します。

```python
# 小目盛りラベルを整列させる
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```
