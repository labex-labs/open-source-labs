# Pruebas con diversos escenarios de fechas

Para entender mejor cómo funciona nuestra función `months_diff` con diferentes escenarios de fechas, creemos un archivo de prueba separado. Este enfoque es común en el desarrollo de software para verificar que nuestro código funcione como se espera.

Crea un nuevo archivo llamado `month_diff_test.py` en el directorio `/home/labex/project`:

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

Guarda este archivo y ejecútalo:

```bash
python3 ~/project/month_diff_test.py
```

Deberías ver una salida similar a:

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

Analicemos estos resultados:

1. **Mismo mes**: Incluso dentro del mismo mes, nuestra función devuelve 1 mes. Esto se debe a que incluso un mes parcial se cuenta como un mes completo.

2. **Meses consecutivos**: Para fechas en meses consecutivos, la función devuelve 1 mes.

3. **A través de años**: Para fechas que cruzan el límite del año, la función sigue calculando correctamente.

4. **Varios meses**: Para fechas que están separadas por varios meses, la función calcula el número adecuado de meses.

5. **Orden inverso**: Cuando la fecha final es anterior a la fecha inicial, obtenemos un resultado negativo, lo cual tiene sentido para escenarios como el cálculo del tiempo restante.

6. **Múltiplos exactos**: Para exactamente 30 días, obtenemos 1 mes. Para 60 días, obtenemos 2 meses. Esto confirma que nuestra función funciona como se espera con múltiplos exactos de nuestra definición de mes.

Nuestra función `months_diff` maneja todos estos casos de prueba de acuerdo con nuestra definición de un mes como 30 días.
