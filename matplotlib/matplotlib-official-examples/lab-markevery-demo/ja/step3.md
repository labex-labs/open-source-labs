# 対数スケールでプロットを作成する

前のステップを繰り返しますが、今回は対数スケールを使用します。対数スケールは、整数ベースのサブサンプリングにおいてマーカー間隔に視覚的な非対称性を引き起こしますが、分数ベースのサブサンプリングでは均等な分布が生成されます。

```python
# 対数スケールでプロットを作成する
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
