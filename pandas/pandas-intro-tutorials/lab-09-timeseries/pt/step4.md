# Calcular a concentração média de NO2 para cada dia da semana

Agora podemos calcular a concentração média de NO2 para cada dia da semana em cada local de medição. Isso pode ser feito usando o método `groupby`.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
