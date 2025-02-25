# 日付と差分を定義する

次に、datetimeライブラリを使用して日付と差分値を定義します。日付範囲は2000年3月2日から2000年3月6日までで、6時間間隔です。次のコードをコピーして貼り付けます。

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
