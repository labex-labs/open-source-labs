# Conectando os Eixos

Nesta etapa, conectaremos os eixos e criaremos o efeito de zoom. Criaremos uma figura com quatro eixos e os conectaremos usando as funções `zoom_effect01` e `zoom_effect02`.

```python
axs = plt.figure().subplot_mosaic([
    ["zoom1", "zoom2"],
    ["main", "main"],
])

axs["main"].set(xlim=(0, 5))
zoom_effect01(axs["zoom1"], axs["main"], 0.2, 0.8)
axs["zoom2"].set(xlim=(2, 3))
zoom_effect02(axs["zoom2"], axs["main"])

plt.show()
```
