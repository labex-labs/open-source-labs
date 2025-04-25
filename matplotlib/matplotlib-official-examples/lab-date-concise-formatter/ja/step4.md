# 日付フォーマットのローカライゼーション

デフォルトのフォーマットが望ましくない場合、日付フォーマットをローカライズすることができます。これは、3 つの文字列のリストのいずれかを操作することで行われます。ISO の「年 月 日」ではなく、ラベルを「日 月 年」に変更します。

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))

for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator()
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = ['%y',  # 目盛りは主に年
                         '%b',       # 目盛りは主に月
                         '%d',       # 目盛りは主に日
                         '%H:%M',    # 時
                         '%H:%M',    # 分
                         '%S.%f', ]  # 秒
    # これらは主に上のレベルと同じです...
    formatter.zero_formats = [''] + formatter.formats[:-1]
    #...ただし、目盛りが主に時間の場合を除き、
    # 月 - 日が欲しい場合があります：
    formatter.zero_formats[3] = '%d-%b'

    formatter.offset_formats = ['',
                                '%Y',
                                '%b %Y',
                                '%d %b %Y',
                                '%d %b %Y',
                                '%d %b %Y %H:%M', ]
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```
