# Graficar la fórmula de demostración del encabezado

En este paso, graficaremos la fórmula de demostración del encabezado.

```python
full_demo = mathtext_demos['Header demo']
ax.annotate(full_demo,
            xy=(0.5, 1. - 0.59 * line_axesfrac),
            color='tab:orange', ha='center', fontsize=20)
```
