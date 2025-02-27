# Daten generieren

Wir werden einen synthetischen Datensatz mit nur 3 informativen Merkmalen generieren. Wir werden ausdrücklich den Datensatz nicht mischen, um sicherzustellen, dass die informativen Merkmale den drei ersten Spalten von X entsprechen. Darüber hinaus werden wir unseren Datensatz in Trainings- und Testuntergruppen aufteilen.

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
