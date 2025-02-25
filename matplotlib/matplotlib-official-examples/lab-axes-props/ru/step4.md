# Настроить свойства делений осей и сетки

Мы можем настроить свойства делений осей и сетки с помощью функций `grid()` и `tick_params()`. В этом примере мы изменим цвет и размер меток делений, а также ширину и стиль линий сетки.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
