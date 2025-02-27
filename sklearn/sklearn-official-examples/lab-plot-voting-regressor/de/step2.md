# Laden des Diabetes-Datensatzes

Als nächstes laden wir den Diabetes-Datensatz in unser Programm mit der Funktion `load_diabetes()`, die von scikit-learn bereitgestellt wird. Diese Funktion gibt den Datensatz als Tupel aus zwei Arrays zurück - eines enthält die Merkmalsdaten und das andere die Zielwerte. Wir werden diese Arrays jeweils `X` und `y` zuweisen.

```python
# Load the diabetes dataset
X, y = load_diabetes(return_X_y=True)
```
