# Crear una aplicación práctica: Calculadora de suscripciones

Ahora que tenemos una función confiable para calcular la diferencia en meses, apliquémosla a un escenario del mundo real. Crearemos una calculadora de suscripciones que determine el costo de una suscripción a un servicio entre dos fechas.

Crea un nuevo archivo llamado `subscription_calculator.py` en el directorio `/home/labex/project`:

```python
from datetime import date, timedelta
from month_difference import months_diff

def calculate_subscription_cost(start_date, end_date, monthly_fee):
    """
    Calculate the total cost of a subscription between two dates.

    Args:
        start_date (date): Subscription start date
        end_date (date): Subscription end date
        monthly_fee (float): Cost per month

    Returns:
        float: Total subscription cost
    """
    # Calculate number of months
    months = months_diff(start_date, end_date)

    # Calculate total cost
    total_cost = months * monthly_fee

    return total_cost

# Example: Calculate subscription cost for a streaming service
start = date(2023, 1, 15)  # Subscription starts January 15, 2023
end = date(2023, 8, 20)    # Ends August 20, 2023
monthly_cost = 9.99        # $9.99 per month

total = calculate_subscription_cost(start, end, monthly_cost)
print(f"Subscription period: {start} to {end}")
print(f"Monthly fee: ${monthly_cost:.2f}")
print(f"Total cost: ${total:.2f}")

# Compare with an annual plan
annual_cost = 99.99  # $99.99 per year
print(f"\nAnnual plan cost: ${annual_cost:.2f}")
print(f"Monthly plan for same period: ${total:.2f}")

if total > annual_cost:
    print(f"Savings with annual plan: ${total - annual_cost:.2f}")
else:
    print(f"Additional cost for annual plan: ${annual_cost - total:.2f}")

# Calculate cost for a trial period
today = date.today()
trial_end = today + timedelta(days=7)  # 7-day trial
trial_cost = calculate_subscription_cost(today, trial_end, monthly_cost)
print(f"\nOne-week trial period: {today} to {trial_end}")
print(f"Trial period cost: ${trial_cost:.2f}")
```

Guarda el archivo y ejecútalo:

```bash
python3 ~/project/subscription_calculator.py
```

Deberías ver una salida similar a esta (las fechas de la prueba mostrarán tu fecha actual):

```
Subscription period: 2023-01-15 to 2023-08-20
Monthly fee: $9.99
Total cost: $79.92

Annual plan cost: $99.99
Monthly plan for same period: $79.92
Additional cost for annual plan: $20.07

One-week trial period: 2023-06-01 to 2023-06-08
Trial period cost: $9.99
```

Esta aplicación demuestra cómo se puede utilizar nuestra función `months_diff` en un escenario práctico:

1. Calculamos el costo total de una suscripción en función del número de meses entre dos fechas.
2. Comparamos este costo con un plan anual para ayudar a un usuario a decidir qué plan es más económico.
3. Calculamos el costo de un período de prueba corto.

Observa cómo incluso la prueba de 7 días se cobra como un mes completo en nuestro modelo. Esto se debe a que nuestra función redondea cualquier mes parcial a un mes completo, lo cual es común en la facturación de suscripciones.

Este tipo de cálculo se utiliza con frecuencia en:

- Servicios de suscripción (streaming, software, membresías)
- Cálculos de préstamos y hipotecas
- Contratos de alquiler
- Facturación de proyectos
