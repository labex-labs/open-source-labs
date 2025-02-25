# Créer le graphique en chapeau

Dans cette étape, nous allons créer le graphique en chapeau à l'aide des données préparées dans l'étape précédente et de la fonction `hat_graph`.

```python
fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Games')
ax.set_ylabel('Score')
ax.set_ylim(0, 60)
ax.set_title('Scores by number of game and players')
ax.legend()

fig.tight_layout()
plt.show()
```
