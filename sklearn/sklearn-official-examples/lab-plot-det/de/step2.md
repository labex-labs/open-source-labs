# Die Klassifizierer definieren

Wir werden zwei verschiedene Klassifizierer definieren, um ihre statistische Leistung über Schwellenwerte mit ROC - und DET - Kurven zu vergleichen. Wir werden die Funktion `make_pipeline` von scikit - learn verwenden, um einen Pipeline zu erstellen, der die Daten mit `StandardScaler` skaliert und einen `LinearSVC` - Klassifizierer trainiert. Wir werden auch die Klasse `RandomForestClassifier` von scikit - learn verwenden, um einen Random - Forest - Klassifizierer mit einer maximalen Tiefe von 5, 10 Schätzern und einem maximalen von 1 Merkmal zu trainieren.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
