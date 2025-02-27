# Teile den Datensatz auf

Als nächstes teilen wir den Datensatz in Trainings- und Testsets auf. Wir werden 80% der Daten zum Training und 20% zum Testen verwenden.

```python
# Teile die Daten in Trainings-/Testsets auf
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Teile die Zielwerte in Trainings-/Testsets auf
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```
