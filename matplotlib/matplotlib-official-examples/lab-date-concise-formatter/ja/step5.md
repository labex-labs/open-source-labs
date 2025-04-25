# ローカライゼーション付きのコンバータの登録

キーワード引数を `~.dates.ConciseDateConverter` に渡し、使用するデータ型を単位レジストリに登録することで、ローカライゼーション付きのコンバータを登録することもできます。

```python
import datetime

formats = ['%y',          # 目盛りは主に年
           '%b',     # 目盛りは主に月
           '%d',     # 目盛りは主に日
           '%H:%M',  # 時
           '%H:%M',  # 分
           '%S.%f', ]  # 秒
# これらは同じでも良いですが、1 つレベルオフセットさせます...
zero_formats = [''] + formats[:-1]
#...ただし、目盛りが主に時間の場合を除き、月 - 日が欲しいです
zero_formats[3] = '%d-%b'
offset_formats = ['',
                  '%Y',
                  '%b %Y',
                  '%d %b %Y',
                  '%d %b %Y',
                  '%d %b %Y %H:%M', ]

converter = mdates.ConciseDateConverter(
    formats=formats, zero_formats=zero_formats, offset_formats=offset_formats)

munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter registered non-default')
plt.show()
```
