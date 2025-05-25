# Figure 및 Axes 생성

바코드를 위한 figure 와 axes 를 생성해야 합니다. figure 크기를 데이터 포인트 수의 배수로 설정하고, 모든 축을 끕니다.

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
```
