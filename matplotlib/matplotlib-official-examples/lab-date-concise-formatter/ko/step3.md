# 변환기 등록

날짜가 있는 모든 축 호출이 이 변환기를 사용하여 이루어지도록 하려면, 단위 레지스트리 (units registry) 를 사용하는 것이 가장 편리할 것입니다. 우리는 단위 레지스트리에 변환기를 등록하고 간결한 날짜 형식 지정자를 사용하여 데이터를 플롯합니다.

```python
import datetime
import matplotlib.units as munits

converter = mdates.ConciseDateConverter()
munits.registry[np.datetime64] = converter
munits.registry[datetime.date] = converter
munits.registry[datetime.datetime] = converter

fig, axs = plt.subplots(3, 1, figsize=(6, 6), layout='constrained')
for nn, ax in enumerate(axs):
    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```
