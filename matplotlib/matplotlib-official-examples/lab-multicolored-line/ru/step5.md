# Создаем цветовую шкалу

Создадим цветовую шкалу для отображения соответствия между цветами и значениями `dydx`. Используем функцию `colorbar` из `matplotlib.pyplot` для создания цветовой шкалы.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
