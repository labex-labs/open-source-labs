# Définir les valeurs d'erreur

Nous allons maintenant définir nos valeurs d'erreur. Dans cet exemple, nous utiliserons la variable `erreur` pour représenter une erreur symétrique et la variable `erreur_asymétrique` pour représenter une erreur asymétrique.

```python
# example error bar values that vary with x-position
error = 0.1 + 0.2 * x

# error bar values w/ different -/+ errors that
# also vary with the x-position
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
