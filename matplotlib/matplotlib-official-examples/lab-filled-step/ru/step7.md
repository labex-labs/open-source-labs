# Создаем гистограмму с штриховкой и заливкой

Мы создадим гистограмму с штриховкой и заливкой с использованием функции `stack_hist`, которую мы определили ранее. Мы будем использовать `stack_data`, `color_cycle` и `hist_func`, которые мы определили ранее. Мы также настроим `plot_kwargs` для включения цвета границ и ориентации.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')
```
