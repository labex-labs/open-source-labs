# Criando uma Figura com Subplots

Agora, criaremos uma figura com quatro subplots, um para cada conjunto de dados. Também definiremos os limites de x e y para serem os mesmos para todos os subplots.

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```
