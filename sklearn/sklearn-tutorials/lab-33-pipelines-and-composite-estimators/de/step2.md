# Verschachtelte Parameter

Sie können die Parameter der Schätzer in einer Pipeline über die Syntax `<Schätzer>__<Parameter>` zugreifen. Dies ist nützlich, um Grid-Searches über die Parameter aller Schätzer in der Pipeline durchzuführen. Hier ist ein Beispiel:

```python
pipe.set_params(clf__C=10)
```
