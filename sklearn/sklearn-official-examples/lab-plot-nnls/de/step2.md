# Daten in Trainings- und Testsets unterteilen

Wir werden unsere Daten in ein Trainingsset und ein Testset unterteilen, wobei jeder Satz 50% der Daten enthält.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
