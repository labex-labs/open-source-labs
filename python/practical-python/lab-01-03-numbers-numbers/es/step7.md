# Ejercicio 1.7: Hipoteca de Dave

Dave ha decidido tomar una hipoteca fija de 30 años por \$500,000 con la corporación de hipotecas, inversión en acciones y trading de Bitcoin de Guido. La tasa de interés es del 5% y el pago mensual es de \$2684.11.

A continuación, hay un programa que calcula la cantidad total que Dave tendrá que pagar durante la vida de la hipoteca:

```python
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
```

Ingrese este programa y ejecútelo. Debería obtener una respuesta de `966279.5999999957`.
