# Création d'un schéma de couleurs

Nous allons créer un schéma de couleurs pour le tableau en utilisant la fonction `plt.cm.BuPu`. Nous utiliserons une teinte pastel de bleu et de violet pour les lignes.

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```
