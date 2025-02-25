# Построить текст с правильным вращением

Наконец, мы построим текст в указанных местах, учитывая вращение линии. В результате текст будет вращаться под правильным углом относительно линии.

```python
# Plot text
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
