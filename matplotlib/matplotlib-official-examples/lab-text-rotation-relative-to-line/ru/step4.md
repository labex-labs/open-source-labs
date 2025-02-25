# Построить текст с неправильным вращением

Теперь мы построим текст в указанных местах, не учитывая вращение линии. В результате текст будет вращаться под углом 45 градусов, что не то, что мы хотим.

```python
# Plot text
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
