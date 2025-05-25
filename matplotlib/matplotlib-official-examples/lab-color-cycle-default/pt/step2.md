# Definir o ciclo de propriedades e obter as cores

Em seguida, precisamos definir o ciclo de propriedades e obter as cores dele.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```
