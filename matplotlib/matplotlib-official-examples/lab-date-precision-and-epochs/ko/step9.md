# 플로팅 (Plotting)

이 단계에서는 에포크가 플로팅에 미치는 영향을 보여줍니다. 이전 기본 에포크를 사용하면 내부 `date2num` 변환 중에 시간이 반올림되어 데이터에 점프가 발생했습니다.

```python
mdates.set_epoch('0000-12-31T00:00:00')

x = np.arange('2000-01-01T00:00:00.0', '2000-01-01T00:00:00.000100', dtype='datetime64[us]')
xold = np.array([mdates.num2date(mdates.date2num(d)) for d in x])
y = np.arange(0, len(x))

fig, ax = plt.subplots(layout='constrained')
ax.plot(xold, y)
ax.set_title('Epoch: ' + mdates.get_epoch())
ax.xaxis.set_tick_params(rotation=40)
plt.show()
```

더 최근의 에포크를 사용하여 플로팅된 날짜의 경우, 플롯은 부드럽습니다.

```python
mdates.set_epoch('1970-01-01T00:00:00')

fig, ax = plt.subplots(layout='constrained')
ax.plot(x, y)
ax.set_title('Epoch: ' + mdates.get_epoch())
ax.xaxis.set_tick_params(rotation=40)
plt.show()
```
