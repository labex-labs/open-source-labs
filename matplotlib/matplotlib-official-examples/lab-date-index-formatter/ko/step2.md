# 주말에 기본 간격으로 데이터 플로팅

먼저 matplotlib 의 `plot` 함수를 사용하여 주말에 기본 간격으로 데이터를 플로팅합니다. 또한 흰색 점선으로 일일 데이터의 간격을 강조 표시합니다.

```python
# Plot data with gaps on weekends
fig, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(r.date, r.adj_close, 'o-')

# Highlight gaps in daily data
gaps = np.flatnonzero(np.diff(r.date) > np.timedelta64(1, 'D'))
for gap in r[['date', 'adj_close']][np.stack((gaps, gaps + 1)).T]:
    ax1.plot(gap.date, gap.adj_close, 'w--', lw=2)
ax1.legend(handles=[ml.Line2D([], [], ls='--', label='Gaps in daily data')])

ax1.set_title("Plotting Data with Default Gaps on Weekends")
ax1.xaxis.set_major_locator(DayLocator())
ax1.xaxis.set_major_formatter(DateFormatter('%a'))
```
