# 해치 (hatch) 로 채워진 히스토그램 생성

앞서 정의한 `stack_hist` 함수를 사용하여 해치로 채워진 히스토그램을 생성합니다. 앞서 정의한 `stack_data`, `color_cycle`, 그리고 `hist_func`를 사용합니다. 또한 `plot_kwargs`를 설정하여 edgecolor 와 orientation 을 포함시킵니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')
```
