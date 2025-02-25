# 極座標プロットを作成する

最後に、極座標プロットで `markevery` がどのように動作するかを示すために、サブプロットのセットを作成します。その動作は線形スケールの場合と似ていることに注目してください。

```python
# 極座標プロットを作成する
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```
