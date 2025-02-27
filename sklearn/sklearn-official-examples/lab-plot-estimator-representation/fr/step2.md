# Représentation HTML riche

La deuxième façon dont nous pouvons afficher des estimateurs est à travers une représentation HTML riche. Dans les notebooks, les estimateurs et les pipelines utiliseront une représentation HTML riche. Cela est particulièrement utile pour résumer la structure des pipelines et d'autres estimateurs composites, avec une interaction pour fournir des détails.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# Créez des pipelines pour les données numériques et catégorielles
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# Créez un prétraiteur qui applique les pipelines numériques et catégorielles à des colonnes spécifiques
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# Créez un pipeline qui applique le prétraiteur et la régression logistique
clf = make_pipeline(preprocessor, LogisticRegression())

# Affichez le pipeline
clf
```
