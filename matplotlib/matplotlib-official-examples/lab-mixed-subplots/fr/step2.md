# Définition des fonctions

Dans cette étape, nous allons définir une fonction qui génère une oscillation amortie.

```python
def f(t):
    return np.cos(2*np.pi*t) * np.exp(-t)
```
