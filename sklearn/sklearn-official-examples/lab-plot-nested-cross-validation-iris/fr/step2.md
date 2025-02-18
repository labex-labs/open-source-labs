# Définir les hyperparamètres

Ensuite, nous définissons les hyperparamètres à optimiser pour le classifieur à vecteurs de support (support vector classifier). Dans ce cas, nous optimisons le paramètre de coût `C` et le coefficient du noyau `gamma`.

```python
# Set up possible values of parameters to optimize over
p_grid = {"C": [1, 10, 100], "gamma": [0.01, 0.1]}
```
