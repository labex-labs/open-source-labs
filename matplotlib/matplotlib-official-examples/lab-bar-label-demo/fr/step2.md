# Étiquetage des diagrammes en barres verticales

Nous commencerons par créer un diagramme en barres verticales et l'étiqueter à l'aide de la fonction `bar_label`. Les données que nous utiliserons sont le nombre de pingouins par sexe, issues de https://allisonhorst.github.io/palmerpenguins/.

```python
species = ('Adelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6  # la largeur des barres : peut également être une séquence de longueur len(x)

fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Nombre de pingouins par sexe')
ax.legend()

plt.show()
```
