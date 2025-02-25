# Пишем подписи к каждой основной трехмерной плоскости обзора

Мы используем функцию `annotate_axes`, определенную на шаге 2, чтобы подписать каждую основную трехмерную плоскость обзора своими соответствующими углами.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
