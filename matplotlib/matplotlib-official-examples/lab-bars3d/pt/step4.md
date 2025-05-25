# Personalizar os Gráficos de Barras

Agora, personalizaremos os gráficos de barras. Criaremos um array de cores e usaremos o método `bar()` para plotar os gráficos de barras. Definiremos o parâmetro `zdir` como 'y' para projetar os gráficos de barras nos planos do eixo y. Também definiremos o parâmetro `alpha` como 0.8 para ajustar a transparência das barras.

```python
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)
```
