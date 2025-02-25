# Créer la fonction de mise à jour

La fonction de mise à jour sera appelée par l'objet `FuncAnimation` pour mettre à jour le nuage de points lors de l'animation.

```python
def update(frame_number):
    # Obtenez un index que nous pouvons utiliser pour redémarrer la plus ancienne goutte de pluie.
    current_index = frame_number % n_drops

    # Rendre toutes les couleurs plus transparentes au fur et à mesure que le temps passe.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Rendre tous les cercles plus grands.
    rain_drops['size'] += rain_drops['growth']

    # Choisissez une nouvelle position pour la plus ancienne goutte de pluie, en remettant à zéro sa taille,
    # sa couleur et son facteur de croissance.
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (0, 0, 0, 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Mettez à jour la collection de points dispersés, avec les nouvelles couleurs, tailles et positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
```
