# バーチャートを作成する

次のステップは、バーチャートを作成することです。チャートを作成するために`bar()`関数を使用します。茶用とコーヒー用の2セットのバーを作成します。また、チャートに誤差棒も追加します。

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```
