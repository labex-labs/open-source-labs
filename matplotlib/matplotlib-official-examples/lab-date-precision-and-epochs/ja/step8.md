# numpy.datetime64 を Matplotlib 日付に変換する

`numpy.datetime64`オブジェクトは、`.datetime`オブジェクトよりもはるかに大きな時間空間に対してマイクロ秒精度を持っています。ただし、現在、Matplotlib の時間は、マイクロ秒解像度と 0000 から 9999 までの年のみを持つ datetime オブジェクトに戻されるだけです。

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
