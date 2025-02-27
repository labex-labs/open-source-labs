# Lade den Datensatz

Zunächst müssen wir einen Datensatz laden, den wir verwenden können, um unser prädiktives Modell zu trainieren. Wir werden den Diabetes-Datensatz aus scikit-learn verwenden, der Informationen über Diabetes-Patienten enthält.

```python
from sklearn.datasets import load_diabetes

# Lade den Diabetes-Datensatz
diabetes = load_diabetes()

# Teile die Daten in Trainings- und Validierungssätze auf
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```
