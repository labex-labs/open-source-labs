# Criar Gráfico de Dispersão

Nesta etapa, criaremos um gráfico de dispersão usando os dados aleatórios da Etapa 2.

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```
