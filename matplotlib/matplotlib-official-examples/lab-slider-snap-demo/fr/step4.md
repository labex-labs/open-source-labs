# Définir les valeurs autorisées pour le curseur d'amplitude

Dans cette étape, vous allez définir les valeurs autorisées pour le curseur d'amplitude. Le curseur d'amplitude utilisera ces valeurs pour s'arrêter sur la valeur autorisée la plus proche.

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
