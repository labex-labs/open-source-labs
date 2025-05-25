# Configurar o Gráfico

Agora, configuraremos o gráfico para nossa simulação. Criaremos uma figura com um limite em x e y igual ao comprimento máximo do pêndulo, definiremos a proporção (aspect ratio) para ser igual e adicionaremos uma grade.

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
