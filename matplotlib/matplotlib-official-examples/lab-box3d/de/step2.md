# Falsche Daten erstellen

Erstellen Sie falsche Daten zum Plotten, indem Sie eine Formel verwenden, um die Daten basierend auf den Werten von X, Y und Z zu berechnen. Wir werden eins zur Ergebnis hinzuaddieren, um sicherzustellen, dass der minimale Wert größer als Null ist.

```python
# Create fake data
data = (((X+100)**2 + (Y-20)**2 + 2*Z)/1000+1)
```
