# Définition de la plage d'hyperparamètres

Nous allons définir une plage de valeurs pour le paramètre gamma du noyau SVM que nous souhaitons tester.

```python
param_range = np.logspace(-6, -1, 5)
```
