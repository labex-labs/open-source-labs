# Realizando operaciones con arrays de enteros anulables

Puedes realizar diversas operaciones con arrays de enteros anulables, como operaciones aritméticas, comparaciones y segmentación.

```python
# Crear una Serie con tipo de entero anulable
s = pd.Series([1, 2, None], dtype="Int64")

# Realizar una operación aritmética
s_plus_one = s + 1 # suma 1 a cada elemento de la serie

# Realizar una comparación
comparison = s == 1 # comprueba si cada elemento de la serie es igual a 1

# Realizar una operación de segmentación
sliced = s.iloc[1:3] # selecciona el segundo y tercer elementos de la serie
```
