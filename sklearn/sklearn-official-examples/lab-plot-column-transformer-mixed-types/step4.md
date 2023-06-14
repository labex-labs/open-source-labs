# Define the Preprocessor

In this step, we will define the `ColumnTransformer` that will be used to preprocess our data.

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
```


