# Crear un objeto BubbleChart y graficar el gráfico

Para crear el gráfico de burbujas empaquetadas, necesitamos crear un objeto `BubbleChart` y llamar al método `collapse` para mover las burbujas hacia el centro de masa. Luego podemos crear una figura de `matplotlib` y agregar un objeto de ejes a ella. Finalmente, llamamos al método `plot` para dibujar las burbujas en el gráfico.

```python
bubble_chart = BubbleChart(area=browser_market_share['market_share'],
                           bubble_spacing=0.1)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
bubble_chart.plot(
    ax, browser_market_share['browsers'], browser_market_share['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title('Browser market share')

plt.show()
```
