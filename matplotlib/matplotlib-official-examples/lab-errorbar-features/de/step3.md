# Fehlerwerte definieren

Wir definieren jetzt unsere Fehlerwerte. In diesem Beispiel verwenden wir die Variable `error`, um symmetrische Fehler zu repräsentieren, und die Variable `asymmetric_error`, um asymmetrische Fehler zu repräsentieren.

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
