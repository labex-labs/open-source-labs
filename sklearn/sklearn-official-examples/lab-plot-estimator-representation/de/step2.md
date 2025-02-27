# Reiche HTML-Repräsentation

Die zweite Möglichkeit, Schätzer anzuzeigen, besteht darin, eine reiche HTML-Repräsentation zu verwenden. In Notebooks werden Schätzer und Pipelines eine reiche HTML-Repräsentation verwenden. Dies ist besonders nützlich, um die Struktur von Pipelines und anderen zusammengesetzten Schätzern zu zusammenfassen, mit Interaktivität, um Details bereitzustellen.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# Erstellen von Pipelines für numerische und kategorische Daten
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# Erstellen eines Vorverarbeiters, der die numerischen und kategorischen Pipelines auf bestimmte Spalten anwendet
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# Erstellen einer Pipeline, die den Vorverarbeiter und die logistische Regression anwendet
clf = make_pipeline(preprocessor, LogisticRegression())

# Anzeige der Pipeline
clf
```
