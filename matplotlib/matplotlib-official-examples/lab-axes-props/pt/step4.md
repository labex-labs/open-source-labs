# Personalizar as Propriedades dos Ticks e da Grelha do Eixo

Podemos personalizar as propriedades dos ticks (marcas) e da grelha do eixo usando as funções `grid()` e `tick_params()`. Neste exemplo, mudaremos a cor e o tamanho dos rótulos dos ticks e a largura e o estilo das linhas da grelha.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
