# Carte thermique catégorielle simple

Nous commencerons par définir certaines données. Nous avons besoin d'une liste ou d'un tableau 2D qui définit les données à colorer. Nous avons également besoin de deux listes ou tableaux de catégories. La carte thermique elle-même est un graphique `imshow` avec les étiquettes définies comme les catégories. Nous utiliserons la fonction `text` pour étiqueter les données elles-mêmes en créant un `Text` dans chaque cellule montrant la valeur de cette cellule.

```python
import matplotlib.pyplot as plt
import numpy as np

légumes = ["concombre", "tomate", "laitue", "asperge", "pomme de terre", "blé", "orge"]
fermiers = ["Farmer Joe", "Upland Bros.", "Smith Gardening", "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

récolte = np.array([[0,8, 2,4, 2,5, 3,9, 0,0, 4,0, 0,0],
                    [2,4, 0,0, 4,0, 1,0, 2,7, 0,0, 0,0],
                    [1,1, 2,4, 0,8, 4,3, 1,9, 4,4, 0,0],
                    [0,6, 0,0, 0,3, 0,0, 3,1, 0,0, 0,0],
                    [0,7, 1,7, 0,6, 2,6, 2,2, 6,2, 0,0],
                    [1,3, 1,2, 0,0, 0,0, 3,2, 5,1],
                    [0,1, 2,0, 0,0, 1,4, 0,0, 1,9, 6,3]])

fig, ax = plt.subplots()
im = ax.imshow(récolte)

# Affiche toutes les graduations et les étiquette avec les entrées respectives de la liste
ax.set_xticks(np.arange(len(fermiers)), labels=fermiers)
ax.set_yticks(np.arange(len(légumes)), labels=légumes)

# Fait tourner les étiquettes des graduations et définit leur alignement
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Parcourez les dimensions des données et créez des annotations de texte
for i in range(len(légumes)):
    for j in range(len(fermiers)):
        text = ax.text(j, i, récolte[i, j], ha="center", va="center", color="w")

ax.set_title("Récolte des fermiers locaux (en tonnes/an)")
fig.tight_layout()
plt.show()
```
