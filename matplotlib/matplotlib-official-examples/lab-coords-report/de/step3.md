# Den Plot erstellen

Jetzt, wo wir unsere Daten haben, können wir unseren Plot mit Matplotlib erstellen. In diesem Beispiel werden wir einen Streudiagramm mit der `plot()`-Funktion erstellen.

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```
