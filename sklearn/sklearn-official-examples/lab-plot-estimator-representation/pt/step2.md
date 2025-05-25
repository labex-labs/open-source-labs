# Representação HTML Detalhada

A segunda forma de exibir estimadores é através de uma representação HTML detalhada. Em notebooks, estimadores e pipelines utilizam uma representação HTML detalhada. Isto é particularmente útil para resumir a estrutura de pipelines e outros estimadores compostos, com interatividade para fornecer detalhes.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# Cria pipelines para dados numéricos e categóricos
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# Cria um pré-processador que aplica os pipelines numéricos e categóricos a colunas específicas
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# Cria um pipeline que aplica o pré-processador e a regressão logística
clf = make_pipeline(preprocessor, LogisticRegression())

# Exibe o pipeline
clf
```
