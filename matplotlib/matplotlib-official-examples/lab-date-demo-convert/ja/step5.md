# x軸を設定して日付をフォーマットする

グラフをより読みやすくするために、x軸の範囲を範囲内の最初と最後の日付に設定します。また、メジャーとマイナーのロケータをそれぞれDayLocatorとHourLocatorに設定します。最後に、DateFormatter関数を使って日付をフォーマットします。次のコードをコピーして貼り付けます。

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
