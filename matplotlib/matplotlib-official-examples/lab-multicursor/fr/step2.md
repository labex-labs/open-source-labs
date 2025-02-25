# Création de données

Ensuite, nous allons créer des données pour nos graphiques. Dans cet exemple, nous allons créer trois ondes sinusoïdales avec des fréquences différentes.

```python
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(3*np.pi*t)
s3 = np.sin(4*np.pi*t)
```
