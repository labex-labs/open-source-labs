# Crear una figura con subgráficos

Ahora crearemos una figura con cuatro subgráficos, uno para cada conjunto de datos. También estableceremos los límites x e y para que sean los mismos para todos los subgráficos.

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```
