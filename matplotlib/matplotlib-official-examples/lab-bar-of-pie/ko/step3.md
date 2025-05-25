# 파이 차트 생성

이제 파이 차트를 만들 수 있습니다. 먼저 figure 및 axis 객체를 정의합니다.

```python
# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)
```

그런 다음 파이 차트의 매개변수를 설정하고 플롯합니다.

```python
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)
```
