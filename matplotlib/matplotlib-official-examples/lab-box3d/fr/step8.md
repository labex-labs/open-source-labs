# Ajouter une barre de couleur

Ajoutez une barre de couleur en utilisant la méthode `colorbar`. Nous définirons les paramètres `fraction` et `pad` pour ajuster l'emplacement de la barre de couleur, et définirons l'étiquette pour montrer le nom et les unités des données.

```python
# Colorbar
fig.colorbar(C, ax=ax, fraction=0.02, pad=0.1, label='Name [units]')
```
