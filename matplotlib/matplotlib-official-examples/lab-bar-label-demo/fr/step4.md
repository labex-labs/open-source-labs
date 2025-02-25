# Étiquetage avancé des barres

Dans cette étape, nous allons montrer quelques choses plus avancées que l'on peut faire avec les étiquettes des barres. Nous utiliserons le même diagramme en barres horizontales que dans l'étape précédente.

```python
fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # les étiquettes sont lues de haut en bas
ax.set_xlabel('Performance')
ax.set_title('Combien vite voulez-vous aller aujourd\'hui?')

# Étiquette avec des légendes données, un rembourrage personnalisé et des options d'annotation
ax.bar_label(hbars, labels=[f'±{e:.2f}' for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
```
