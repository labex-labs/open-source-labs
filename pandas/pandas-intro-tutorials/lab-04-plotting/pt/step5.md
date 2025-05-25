# Criando um Gráfico de Dispersão (Scatter Plot)

Para comparar visualmente os valores de NO2 medidos em Londres versus Paris, podemos criar um gráfico de dispersão (scatter plot).

```python
# Criando um gráfico de dispersão
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
