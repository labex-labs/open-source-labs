# Créer des sous-graphiques

Pour créer des sous-graphiques dans Matplotlib, vous pouvez utiliser la méthode `subplot()`. Cette méthode prend trois arguments : le nombre de lignes, le nombre de colonnes et le numéro du graphique. Voici un exemple qui crée trois sous-graphiques :

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```
