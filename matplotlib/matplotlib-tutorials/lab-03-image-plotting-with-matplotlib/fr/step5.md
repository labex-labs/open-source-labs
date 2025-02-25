# Examen de plages de données spécifiques

Parfois, il peut être nécessaire d'examiner des plages de données spécifiques dans une image. Nous pouvons le faire en ajustant les limites de la carte de couleurs à l'aide du paramètre `clim` dans la fonction `imshow`. Cela nous permet de nous concentrer sur des régions spécifiques de l'image tout en sacrifiant le détail dans d'autres régions.

```python
min_value, max_value = 100, 200
plt.imshow(img, clim=(min_value, max_value))
```
