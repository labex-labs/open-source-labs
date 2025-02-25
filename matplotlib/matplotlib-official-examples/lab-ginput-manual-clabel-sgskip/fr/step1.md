# Définir un triangle en cliquant sur trois points

Dans cette étape, nous allons définir un triangle en cliquant sur trois points. Nous utiliserons les fonctions `ginput` et `waitforbuttonpress` pour y arriver. La fonction `ginput` nous permet de sélectionner des points sur le graphique avec la souris, et la fonction `waitforbuttonpress` attend un événement de pression sur un bouton.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)

tellme('Vous allez définir un triangle, cliquez pour commencer')

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme('Sélectionnez 3 coins avec la souris')
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme('Trop peu de points, recommencez')
            time.sleep(1)  # Attendez une seconde

    ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=2)

    tellme('Êtes-vous content? Cliquez sur une touche pour oui, cliquez avec la souris pour non')

    if plt.waitforbuttonpress():
        break

    # Supprimez la zone de remplissage
    for p in ph:
        p.remove()
```
