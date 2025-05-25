# x 축 설정 및 날짜 형식 지정

그래프의 가독성을 높이기 위해 x 축 범위를 범위 내 첫 번째 날짜와 마지막 날짜로 설정합니다. 또한 주요 및 보조 로케이터 (locator) 를 각각 DayLocator 및 HourLocator 로 설정합니다. 마지막으로 DateFormatter 함수를 사용하여 날짜 형식을 지정합니다. 다음 코드를 복사하여 붙여넣으십시오:

```python
ax.set_xlim(dates[0], dates[-1])
ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_minor_locator(HourLocator(range(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
```
