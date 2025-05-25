# numpy.datetime64 를 matplotlib 날짜로 변환

`numpy.datetime64` 객체는 `.datetime` 객체보다 훨씬 더 큰 시간 공간에 대해 마이크로초 정밀도를 갖습니다. 그러나 현재 Matplotlib 시간은 마이크로초 해상도를 가지며 0000 에서 9999 까지의 연도만 포함하는 datetime 객체로만 다시 변환됩니다.

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
