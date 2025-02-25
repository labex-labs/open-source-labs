# Générer les données

Ensuite, nous allons générer les données pour notre graphique. Nous allons créer trois ondes sinusoïdales avec des fréquences différentes en utilisant `numpy`.

```python
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)
```
