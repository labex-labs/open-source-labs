# Ajouter une ligne verticale

Ajoutez des lignes verticales à l'aide de la fonction `axvline()`.

```python
# Ligne verticale à x = 1 qui couvre la plage d'ordonnées.
ax.axvline(x=1)
# Ligne verticale épaisse de couleur bleue à x = 0 qui couvre le quart supérieur de la plage d'ordonnées.
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
```
