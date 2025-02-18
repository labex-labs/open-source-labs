# Definition der Hyperparameter

Als nächstes definieren wir die Hyperparameter, die für den Support-Vektor-Klassifikator (Support vector classifier) optimiert werden sollen. In diesem Fall optimieren wir den Kostenparameter `C` und den Kernel-Koeffizienten `gamma`.

```python
# Set up possible values of parameters to optimize over
p_grid = {"C": [1, 10, 100], "gamma": [0.01, 0.1]}
```
