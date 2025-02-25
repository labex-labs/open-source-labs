# Créer des données pour le graphique en ligne

Dans cette étape, nous allons créer des données pour notre graphique en ligne. Nous utiliserons la fonction `linspace` de NumPy pour créer un tableau de valeurs régulièrement espacées entre 0 et 10. Nous générerons également du bruit aléatoire à l'aide de la fonction `random.randn` de NumPy.

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```
