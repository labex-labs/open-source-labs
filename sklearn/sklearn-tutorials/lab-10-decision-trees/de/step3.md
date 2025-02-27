# Aufteilen des Datensatzes

Bevor wir den Entscheidungsbaum-Klassifikator (Decision Tree classifier) trainieren, müssen wir den Datensatz in Trainings- und Testdatensätze aufteilen. Wir werden 70 % der Daten zum Training und 30 % zum Testen verwenden.

```python
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
