# Crear un gráfico de dispersión

Para comparar visualmente los valores de NO2 medidas en Londres y París, podemos crear un gráfico de dispersión.

```python
# Creando un gráfico de dispersión
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()
```
