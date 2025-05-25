# Configurar a Formatação dos Rótulos dos Ticks

Configuraremos a formatação dos rótulos dos ticks para nossos subplots. O primeiro subplot usará as configurações padrão, o segundo subplot usará a formatação sofisticada de expressões matemáticas e o terceiro subplot não usará a notação de deslocamento (offset).

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
