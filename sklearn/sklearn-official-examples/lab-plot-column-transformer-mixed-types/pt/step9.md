# Utilizar ColumnTransformer Selecionando Colunas por Tipos de Dados

Neste passo, utilizaremos `ColumnTransformer` selecionando colunas por seus tipos de dados. Usaremos `make_column_selector` para selecionar colunas com base em seus tipos de dados.

```python
from sklearn.compose import make_column_selector as selector

subset_feature = ["embarked", "sex", "pclass", "age", "fare"]
X_train, X_test = X_train[subset_feature], X_test[subset_feature]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, selector(dtype_exclude="category")),
        ("cat", categorical_transformer, selector(dtype_include="category")),
    ]
)
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
