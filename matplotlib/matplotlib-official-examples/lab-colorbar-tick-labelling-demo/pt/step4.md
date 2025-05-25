# Criar um gráfico com uma barra de cores horizontal

Agora criaremos um gráfico com uma barra de cores horizontal. Seguiremos os mesmos passos do Passo 2, mas desta vez usaremos o mapa de cores `afmhot` e definiremos a orientação da barra de cores como horizontal.

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
