# Création des données

Ensuite, nous allons créer les données qui seront utilisées dans le graphique. Nous allons créer trois ondes sinusoïdales différentes avec des fréquences différentes en utilisant la bibliothèque `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)
```
