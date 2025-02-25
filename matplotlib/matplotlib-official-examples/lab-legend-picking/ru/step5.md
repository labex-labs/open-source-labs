# Отображаем линии легенды на исходные линии

Мы сопоставим линии легенды с исходными линиями с использованием словаря.

```python
lines = [line1, line2]
lined = {}  # Будет сопоставлять линии легенды с исходными линиями.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Включает выделение по линии легенды.
    lined[legline] = origline
```
