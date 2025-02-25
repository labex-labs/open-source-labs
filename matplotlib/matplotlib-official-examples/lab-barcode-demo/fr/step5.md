# Rendu du code-barres

Enfin, nous pouvons rendre le code-barres en utilisant `Axes.imshow`. Nous utiliserons `code.reshape(1, -1)` pour convertir les données en un tableau 2D avec une seule ligne, `imshow(..., aspect='auto')` pour autoriser des pixels non carrés, et `imshow(..., interpolation='nearest')` pour éviter les bords flous.

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
