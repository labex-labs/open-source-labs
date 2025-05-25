# 줄기 플롯 생성

다음으로, 가까운 이벤트도 구별할 수 있도록 레벨에 약간의 변화를 주어 줄기 플롯을 생성합니다. 타임라인의 1 차원적인 특성을 시각적으로 강조하기 위해 기준선에 마커를 추가합니다. 각 이벤트에 대해 `~.Axes.annotate`를 통해 텍스트 레이블을 추가하며, 이는 이벤트 선의 끝에서 포인트 단위로 오프셋됩니다. 다음은 줄기 플롯을 생성하는 코드입니다.

```python
# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # The vertical stems.
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # Baseline and markers on it.

# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```
