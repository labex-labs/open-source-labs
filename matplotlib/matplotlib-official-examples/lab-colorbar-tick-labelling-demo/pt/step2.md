# Criar um gráfico com uma barra de cores vertical

Começaremos criando um gráfico com uma barra de cores vertical. Geraremos alguns dados aleatórios usando `randn` de `numpy` e limitaremos os valores ao intervalo de -1 a 1. Em seguida, criaremos um objeto `AxesImage` usando `imshow` e o mapa de cores `coolwarm`. Finalmente, adicionaremos um título ao gráfico.

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
