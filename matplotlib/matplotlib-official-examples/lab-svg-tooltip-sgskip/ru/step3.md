# Сохраняем график в формате SVG

Мы сохраняем график в фиктивный файловый объект с использованием класса `BytesIO` и метода `savefig`.

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
