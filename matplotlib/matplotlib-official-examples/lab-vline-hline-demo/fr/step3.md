# Ajouter du bruit aux données

Dans cette étape, nous allons ajouter du bruit aux données pour les rendre plus réalistes. Nous utiliserons la fonction `normal` de NumPy pour générer des nombres aléatoires avec une moyenne de 0,0 et un écart-type de 0,3.

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
