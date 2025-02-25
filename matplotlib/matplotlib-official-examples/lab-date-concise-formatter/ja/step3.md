# コンバータの登録

日付を持つ軸へのすべての呼び出しがこのコンバータを使用して行われる場合、おそらく最も便利なのは、単位レジストリを使用することです。単位レジストリにコンバータを登録し、簡略化された日付フォーマッタを使用してデータをプロットします。

```python
import datetime
import matplotlib.units as munits

converter = mdates.ConciseDateConverter()
munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, figsize=(6, 6), layout='constrained')
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```
