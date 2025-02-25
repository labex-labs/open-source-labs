# Übung 1.7: Daves Hypothek

Dave hat sich entschieden, eine 30-jährige Festzins-Hypothek von 500.000 US-Dollar bei der Hypotheken-, Aktienanlage- und Bitcoin-Handelskörperschaft von Guido zu nehmen. Der Zinssatz beträgt 5% und die monatliche Rate ist 2684,11 US-Dollar.

Hier ist ein Programm, das den Gesamtbetrag berechnet, den Dave während der Laufzeit der Hypothek zahlen muss:

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

Geben Sie dieses Programm ein und führen Sie es aus. Sie sollten eine Antwort von `966279.5999999957` erhalten.
