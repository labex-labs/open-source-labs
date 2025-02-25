# Настроить форматирование меток делений

Мы настроим форматирование меток делений для наших подграфиков. В первом подграфике будут использоваться стандартные настройки, во втором подграфике будет использоваться элегантное форматирование математических выражений, а в третьем подграфике не будет использоваться смещенная запись.

```python
# Subplot 1 (default settings)
axs[0, 0].set_title("default settings")

# Subplot 2 (useMathText=True)
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# Subplot 3 (useOffset=False)
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```
