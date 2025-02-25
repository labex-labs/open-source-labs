# Definir el ciclo de propiedades y recuperar los colores

A continuación, necesitamos definir el ciclo de propiedades y recuperar los colores de él.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```
