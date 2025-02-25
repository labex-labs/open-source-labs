# Agregando estadísticas agrupadas por categoría

A continuación, aprenderemos a agregar estadísticas agrupadas por categoría.

```python
# Calculando la edad promedio de los pasajeros del Titanic masculinos y femeninos
average_age_sex = titanic[["Sex", "Age"]].groupby("Sex").mean()
# Imprimiendo el resultado
print(f"La edad promedio de los pasajeros del Titanic masculinos y femeninos es {average_age_sex}")

# Calculando el precio promedio de la tarifa del billete para cada combinación de sexo y clase de camarote
mean_fare_sex_class = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# Imprimiendo el resultado
print(f"El precio promedio de la tarifa del billete para cada combinación de sexo y clase de camarote es {mean_fare_sex_class}")
```
