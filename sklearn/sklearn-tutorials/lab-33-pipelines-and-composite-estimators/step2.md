# Nested Parameters

You can access the parameters of the estimators in a pipeline using the syntax `<estimator>__<parameter>`. This is useful for doing grid searches over the parameters of all estimators in the pipeline. Here is an example:

```python
pipe.set_params(clf__C=10)
```
