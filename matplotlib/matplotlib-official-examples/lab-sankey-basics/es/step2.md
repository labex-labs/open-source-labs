# Crear un diagrama de Sankey simple

Comenzaremos creando un diagrama de Sankey simple que demuestra cómo usar la clase Sankey.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

Este código generará un diagrama de Sankey con configuraciones predeterminadas, que incluye las etiquetas y orientaciones de los flujos. El diagrama resultante se mostrará con el título "The default settings produce a diagram like this."
