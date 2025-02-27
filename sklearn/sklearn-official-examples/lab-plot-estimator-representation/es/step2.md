# Representación HTML detallada

La segunda forma en que podemos mostrar estimadores es a través de una representación HTML detallada. En los cuadernos, los estimadores y las tuberías utilizarán una representación HTML detallada. Esto es particularmente útil para resumir la estructura de las tuberías y otros estimadores compuestos, con interactividad para proporcionar detalles.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# Crea tuberías para datos numéricos y categóricos
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# Crea un preprocesador que aplica las tuberías numéricas y categóricas a columnas específicas
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# Crea una tubería que aplica el preprocesador y la regresión logística
clf = make_pipeline(preprocessor, LogisticRegression())

# Muestra la tubería
clf
```
