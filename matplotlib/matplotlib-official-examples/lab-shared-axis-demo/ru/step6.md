# Удаляем метки делений

Мы можем удалить метки делений из конкретного подграфика, изменив видимость меток с использованием метода `ax.get_xticklabels()`. В этом примере мы удалим метки делений на оси x второго подграфика.

```python
plt.tick_params('x', labelbottom=False)
```
