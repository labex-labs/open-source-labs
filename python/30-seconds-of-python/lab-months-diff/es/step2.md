# Crear la función de diferencia en meses

Ahora que entendemos cómo trabajar con objetos de fecha y calcular la diferencia en días, creemos una función para calcular la diferencia en meses.

En muchas aplicaciones, un mes se aproxima a 30 días. Si bien esto no siempre es preciso (los meses pueden tener de 28 a 31 días), es una simplificación común que funciona bien para muchos cálculos comerciales.

Abre tu archivo `month_difference.py` y agrega esta función debajo de tu código existente:

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

Entendamos qué hace esta función:

1. Toma dos parámetros: `start` y `end`, que son objetos de fecha.
2. Calcula la diferencia en días entre estas fechas.
3. Divide por 30 para convertir los días en meses.
4. Utiliza `ceil()` para redondear hacia arriba al entero más cercano.
5. Devuelve el resultado como un entero.

La función `ceil()` se utiliza porque en muchos escenarios comerciales, incluso un mes parcial se cuenta como un mes completo con fines de facturación.

Para probar nuestra función, agrega el siguiente código al final de tu archivo:

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

Guarda tu archivo y ejecútalo nuevamente:

```bash
python3 ~/project/month_difference.py
```

Deberías ver una salida como esta:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

Observa que:

- Los 64 días entre el 15 de enero de 2023 y el 20 de marzo de 2023 se calculan como 3 meses (64/30 = 2.13, redondeado hacia arriba a 3).
- La diferencia entre el 28 de octubre y el 25 de noviembre se calcula como 1 mes.
- La diferencia entre el 15 de diciembre y el 10 de enero (a través de un límite de año) también se calcula como 1 mes.
