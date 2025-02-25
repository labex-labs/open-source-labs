# Définir les données

L'étape suivante est de définir les données que nous utiliserons dans notre graphique. Nous utiliserons la fonction `arange` de NumPy pour créer un tableau de valeurs allant de 0 à 5 avec un pas de 0,1. Nous utiliserons ce tableau comme axe des abscisses. Nous définirons également l'axe des ordonnées en utilisant les fonctions exponentielle et sinus de NumPy.

```python
# Define the data
t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
```
