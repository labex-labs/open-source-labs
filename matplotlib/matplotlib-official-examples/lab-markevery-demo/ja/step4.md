# ズームインしたプロットを作成する

今度は、ズームインしたプロットで `markevery` がどのように動作するかを示すために、もう一組のサブプロットを作成します。整数ベースのサブサンプリングは、元のデータからポイントを選択し、ビューとは独立していることに注目してください。一方、浮動小数点数ベースのサブサンプリングは Axes の対角線に関連しており、表示されるデータ範囲を変更します。

```python
# ズームインしたプロットを作成する
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
