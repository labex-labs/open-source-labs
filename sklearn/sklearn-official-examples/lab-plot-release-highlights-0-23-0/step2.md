# Visualizing Estimators

In scikit-learn 0.23, estimators can be visualized in notebooks by enabling the display='diagram' option. This is particularly useful to summarize the structure of pipelines and other composite estimators, with interactivity to provide detail.

```python
from sklearn import set_config
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# enable display='diagram'
set_config(display="diagram")

# create a pipeline
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)
clf = make_pipeline(preprocessor, LogisticRegression())
clf
```
