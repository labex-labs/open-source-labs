# Добавляем текст на график

Вы можете добавить текст на свой график с использованием функции `ax.text()`. В этом примере мы добавим текст с разными семействами шрифтов.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```
