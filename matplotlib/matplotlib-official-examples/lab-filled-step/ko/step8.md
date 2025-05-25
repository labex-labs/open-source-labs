# 레이블이 지정된 해치 (hatch) 로 채워진 히스토그램 생성

앞서 정의한 `stack_hist` 함수를 사용하여 레이블이 지정된 해치로 채워진 히스토그램을 생성합니다. 앞서 정의한 `dict_data`, `color_cycle`, 그리고 `hist_func`를 사용합니다. 또한 처음과 마지막 세트만 플롯하기 위해 `labels`를 `['set 0', 'set 3']`으로 설정합니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0', 'set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```
