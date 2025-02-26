# チャレンジ

乗車データのスライスを取るとどうなりますか？

```python
>>> r = rows[0:10]
>>> r
... 結果を見る...
>>>
```

おそらく少し奇妙な見た目になるでしょう。`RideData`クラスを修正して、辞書のリストのように見える適切なスライスを生成できるようにできますか？たとえば、このように：

```python
>>> rows = readrides.read_rides_as_columns('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> r = rows[0:10]
>>> r
<readrides.RideData object at 0x10f5068c8>
>>> len(r)
10
>>> r[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> r[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```
