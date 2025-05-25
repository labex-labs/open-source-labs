# Criar Objeto BubbleChart e Plotar o Gráfico

Para criar o gráfico de bolhas empacotadas, precisamos criar um objeto `BubbleChart` e chamar o método `collapse` para mover as bolhas em direção ao centro de massa. Em seguida, podemos criar uma figura `matplotlib` e adicionar um objeto de eixos a ela. Finalmente, chamamos o método `plot` para desenhar as bolhas no gráfico.

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
