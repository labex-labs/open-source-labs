# Adicionar uma legenda ao plot

Agora adicionaremos uma legenda ao plot. Existem duas maneiras de adicionar uma legenda no Matplotlib. Usaremos ambos os métodos neste exemplo.

```python
# Method 1: Place a legend above the subplot
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Method 2: Place a legend to the right of the subplot
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
