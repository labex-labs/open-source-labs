# Создаем гистограмму с штриховкой и заливкой с метками

Мы создадим гистограмму с штриховкой и заливкой с метками с использованием функции `stack_hist`, которую мы определили ранее. Мы будем использовать `dict_data`, `color_cycle` и `hist_func`, которые мы определили ранее. Мы также установим `labels` в `['set 0','set 3']`, чтобы нарисовать только первый и последний набор.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0','set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```
