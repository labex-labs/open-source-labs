# Установка заголовка

В этом шаге вам нужно установить заголовок для каждого графика.

```python
axs[0, 0].set_title('Linear normalization')

for ax, gamma in zip(axs.flat[1:], gammas):
    ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
```
