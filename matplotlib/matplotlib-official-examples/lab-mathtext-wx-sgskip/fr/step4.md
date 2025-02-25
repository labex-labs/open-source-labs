# Définir des fonctions

Définissez une liste de fonctions que l'application affichera. Chaque fonction est définie par un texte mathématique et une fonction lambda qui prend une valeur d'entrée et renvoie une valeur de sortie.

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```
