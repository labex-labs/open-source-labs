# Calculando estadísticas resumidas

En este paso, calcularemos estadísticas resumidas para el conjunto de datos del Titanic.

```python
# Calculando la edad promedio de los pasajeros del Titanic
average_age = titanic["Age"].mean()
# Imprimiendo el resultado
print(f"La edad promedio de los pasajeros del Titanic es {average_age}")

# Calculando la edad mediana y el precio de la tarifa del billete de los pasajeros del Titanic
median_age_fare = titanic[["Age", "Fare"]].median()
# Imprimiendo el resultado
print(f"La edad mediana y el precio de la tarifa del billete de los pasajeros del Titanic son {median_age_fare}")
```
