# 日付と差分を定義する

次に、datetime ライブラリを使用して日付と差分値を定義します。日付範囲は 2000 年 3 月 2 日から 2000 年 3 月 6 日までで、6 時間間隔です。次のコードをコピーして貼り付けます。

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
