# Figure 및 Subplot 생성

다음으로, 플롯을 위한 figure 와 subplot 을 생성해야 합니다. `add_subplot`의 `projection` 매개변수를 사용하여 극좌표 플롯을 생성합니다.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```
