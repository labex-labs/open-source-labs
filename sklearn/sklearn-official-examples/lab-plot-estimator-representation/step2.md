# Rich HTML Representation

The second way we can display estimators is through rich HTML representation. In notebooks, estimators and pipelines will use a rich HTML representation. This is particularly useful to summarize the structure of pipelines and other composite estimators, with interactivity to provide detail.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# Create pipelines for numerical and categorical data
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# Create a preprocessor that applies the numerical and categorical pipelines to specific columns
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# Create a pipeline that applies the preprocessor and logistic regression
clf = make_pipeline(preprocessor, LogisticRegression())

# Display the pipeline
clf
```
