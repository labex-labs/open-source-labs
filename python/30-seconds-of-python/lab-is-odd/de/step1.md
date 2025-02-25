# Prüfen, ob eine Zahl ungerade ist

Schreiben Sie eine Funktion namens `is_odd`, die ein einzelnes Integer als Argument nimmt und `True` zurückgibt, wenn die Zahl ungerade ist, und `False`, wenn die Zahl gerade ist. Ihre Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie den Modulo (`%`)-Operator, um zu überprüfen, ob die Zahl gerade oder ungerade ist.
2. Wenn die Zahl ungerade ist, geben Sie `True` zurück. Wenn die Zahl gerade ist, geben Sie `False` zurück.

```python
def is_odd(num):
  return num % 2!= 0
```

```python
is_odd(3) # True
```
