# Daten erstellen

Als nächstes müssen wir die Daten erstellen, die wir verwenden werden, um den Konturplot zu generieren. Wir werden die `get_test_data()`-Funktion aus dem `mpl_toolkits.mplot3d`-Modul verwenden, um Beispiel-Daten zu generieren.

```python
X, Y, Z = axes3d.get_test_data(0.05)
```
