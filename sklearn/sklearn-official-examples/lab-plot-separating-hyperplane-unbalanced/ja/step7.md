# 凡例を追加する

`matplotlib.pyplot` の `legend` 関数を使って、プロットに凡例を追加します。凡例のラベルをそれぞれ `"non weighted"` と `"weighted"` に設定します。

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```
