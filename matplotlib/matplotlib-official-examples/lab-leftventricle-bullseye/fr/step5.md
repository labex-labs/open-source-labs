# Création d'un camembert

Nous allons créer un camembert avec cinq secteurs représentant différents points de données. Nous utiliserons la fonction `pie` fournie par le module `pyplot` pour créer le camembert.

```python
# Création des données pour le camembert
data = [10, 20, 30, 25, 15]

# Création des étiquettes pour le camembert
labels = ['Donnée 1', 'Donnée 2', 'Donnée 3', 'Donnée 4', 'Donnée 5']

# Création d'un camembert
plt.pie(data, labels=labels)

# Ajout d'un titre au graphique
plt.title('Camembert')

# Affichage du graphique
plt.show()
```
