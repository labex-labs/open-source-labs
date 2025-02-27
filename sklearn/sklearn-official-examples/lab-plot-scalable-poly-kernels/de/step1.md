# Daten laden und vorbereiten

Wir laden zunächst den Covtype-Datensatz und transformieren ihn in ein binäres Klassifizierungsproblem, indem wir nur eine Klasse auswählen. Anschließend teilen wir die Daten in einen Trainingssatz und einen Testsatz auf und normalisieren die Merkmale.

```python
from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer

# Lade den Covtype-Datensatz, wähle nur eine Klasse aus
X, y = fetch_covtype(return_X_y=True)
y[y!= 2] = 0
y[y == 2] = 1

# Teile die Daten in einen Trainingssatz und einen Testsatz auf
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=5000, test_size=10000, random_state=42
)

# Normalisiere die Merkmale
mm = make_pipeline(MinMaxScaler(), Normalizer())
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)
```
