# Добавьте подписи осей и делений на осях

Добавьте подписи к осям x и y с использованием `figtext`. Спрятать верхние и правые контуры с использованием `spines`. Задайте пользовательские позиции делений и подписи с использованием `set_xticks` и `set_yticks`.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
