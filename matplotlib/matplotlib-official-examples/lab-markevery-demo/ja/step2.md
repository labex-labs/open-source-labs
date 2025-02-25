# 線形スケールでプロットを作成する

次に、線形スケールで `markevery` がどのように動作するかを示すために、サブプロットのセットを作成します。`cases` リストを反復処理し、各ケースを個別のサブプロットにプロットします。マークするデータポイントを指定するために `markevery` パラメータを使用します。

```python
# 線形スケールでプロットを作成する
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
