# Figure 및 Subplot 생성

다음으로, figure 를 생성하고 `AxesZero`를 사용하여 subplot 을 추가합니다. 이렇게 하면 x 축 및 y 축 레이블이 있는 축 선이 생성되지만 눈금 표시나 격자는 없습니다.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```
