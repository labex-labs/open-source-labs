# numpy.datetime64をMatplotlib日付に変換する

`numpy.datetime64`オブジェクトは、`.datetime`オブジェクトよりもはるかに大きな時間空間に対してマイクロ秒精度を持っています。ただし、現在、Matplotlibの時間は、マイクロ秒解像度と0000から9999までの年のみを持つdatetimeオブジェクトに戻されるだけです。

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
