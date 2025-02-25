# Étiquetage des diagrammes en barres horizontales

Ensuite, nous allons créer un diagramme en barres horizontales et l'étiqueter à l'aide de la fonction `bar_label`. Nous utiliserons les données de l'étape précédente, mais cette fois-ci, nous allons générer des données de performance aléatoires pour chaque personne.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # les étiquettes sont lues de haut en bas
ax.set_xlabel('Performance')
ax.set_title('Combien vite voulez-vous aller aujourd\'hui?')

# Étiquette avec des flottants formattés spécialement
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # ajuster la limite x pour adapter les étiquettes

plt.show()
```
