# Realizar una operación de ventana con ponderación exponencial

Realizar una operación de ventana con ponderación exponencial y luego calcular la media para cada ventana.

```python
# Realizar una operación de ventana con ponderación exponencial y calcular la media para cada ventana
s.ewm(span=3).mean()
```
