# Créer des sous-graphiques

Nous pouvons créer des sous-graphiques en utilisant la méthode `plt.subplot()`. Dans cet exemple, nous allons créer trois sous-graphiques, le premier occupant la première ligne et les trois colonnes, et les deuxième et troisième sous-graphiques occupant respectivement la deuxième et la troisième ligne, et partageant l'axe x avec le premier sous-graphique.

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```
