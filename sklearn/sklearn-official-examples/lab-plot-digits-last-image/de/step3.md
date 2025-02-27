# Vorbereitung des Datasets für maschinelles Lernen

Bevor wir ein maschinelles Lernmodell auf dem Dataset trainieren können, müssen wir die Daten vorbereiten, indem wir sie in Trainings- und Testsets unterteilen. Wir können dies mit der `train_test_split`-Funktion von scikit-learn tun:

```python
from sklearn.model_selection import train_test_split

# Teilen Sie das Dataset in Trainings- und Testsets auf
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```
