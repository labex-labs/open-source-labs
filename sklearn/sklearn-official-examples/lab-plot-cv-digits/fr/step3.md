# Définir les valeurs des hyperparamètres à tester

Nous allons tester différentes valeurs du paramètre de régularisation C, qui contrôle le compromis entre la maximisation de la marge et la minimisation de l'erreur de classification. Nous allons tester 10 valeurs espacées logarithmiquement entre 10^-10 et 1.

```python
C_s = np.logspace(-10, 0, 10)
```
