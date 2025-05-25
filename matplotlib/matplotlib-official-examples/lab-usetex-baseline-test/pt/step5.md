# Definir os limites e rótulos do gráfico

Definiremos os limites e rótulos do gráfico para corresponder à saída desejada.

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
