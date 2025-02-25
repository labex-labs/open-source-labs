# Redimensionnement d'une image par interpolation 'antialiased'

Enfin, nous allons redimensionner l'image de 500 pixels de données à 530 pixels affichés en utilisant l'interpolation 'antialiased'. Cela démontrera comment l'utilisation d'algorithmes d'antialiasing plus performants peut réduire les motifs de Moiré.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
